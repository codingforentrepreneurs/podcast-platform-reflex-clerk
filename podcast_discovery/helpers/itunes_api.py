import urllib.parse
import requests

PODCAST_LANGUAGES = ["English"]
PODCAST_LANGUAGES = [x.lower() for x in PODCAST_LANGUAGES]

# docs: https://performance-partners.apple.com/search-api
# Constants should be in UPPERCASE and better organized
ITUNES_API_BASE_URL = "https://itunes.apple.com/search"
DEFAULT_TIMEOUT = 10


def url_encode(params):
    return urllib.parse.urlencode(params, quote_via=urllib.parse.quote_plus)


def format_search_url(
    query: str = None,
    attribute: str = "descriptionTerm",
    entity: str = "podcastEpisode",
    limit: int = 20,
    offset: int = 0,
):
    """Build iTunes search URL with parameters"""
    attribute_options = [
        "titleTerm",
        "languageTerm",
        "authorTerm",
        "genreIndex",
        "artistTerm",
        "ratingIndex",
        "keywordsTerm",
        "descriptionTerm",
    ]
    if attribute not in attribute_options:
        attribute = "titleTerm"
    entity_options = ["podcastEpisode", "podcast", "podcastAuthor"]

    if entity not in entity_options:
        entity = "podcast"
    # docs found at https://developer.apple.com/documentation/itunes_store_connect_api/search_for_podcasts_and_episodes
    params = {
        "lang": "en_us",
        "media": "podcast",
        "entity": entity,
        "limit": limit,
        "term": query or "Entrepreneurship",
        "attribute": attribute
    }
    if isinstance(offset, int) and offset > 0:
        params["offset"] = offset
    return f"{ITUNES_API_BASE_URL}?{url_encode(params)}"


def podcast_search(
    query: str,
    limit: int = 20,
    offset: int = 0,
    entity: str = "podcastEpisode",
    attribute: str = "titleTerm",
    sort_by_date: bool = False,
    verbose: bool = False,
):
    """
    Search for podcast episodes using iTunes API.

    Args:
        query (str): Term to search for
        limit (int): Maximum number of results to return
        offset (int): Offset of results to return
        attribute (str): Attribute to search for options include
                        titleTerm,
                        languageTerm, authorTerm, genreIndex, artistTerm,
                        ratingIndex, keywordsTerm, descriptionTerm
        verbose (bool): Whether to print verbose output

    Returns:
        list: Filtered and sorted podcast episodes
    """
    url = format_search_url(
        query=query, 
        entity=entity, 
        attribute=attribute, 
        limit=limit, 
        offset=offset
    )
    if verbose:
        print(f"Searching for {query} with URL: {url}")
    response = requests.get(
        url, headers={"Content-Type": "application/json"}, timeout=DEFAULT_TIMEOUT
    )
    response.raise_for_status()

    results = response.json().get("results", [])
    return _filter_and_sort_results(results, sort_by_date=sort_by_date)


def _filter_and_sort_results(results, sort_by_date=True):
    """Helper function to filter and sort podcast episodes"""
    if sort_by_date:
        return sorted(
                [r for r in results if r.get("kind") == "podcast-episode"],
                key=lambda x: x["releaseDate"],
                reverse=True,
            )
    return [r for r in results if r.get("kind") == "podcast-episode"]