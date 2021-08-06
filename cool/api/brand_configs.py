from cool import utils


def get_the_brand_config_variables_that_should_be_used_for_this_domain(
    session,
    base_url,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get the brand config variables that should be used for this domain

    `GET /api/v1/brand_variables`

    Will redirect to a static json file that has all of the brand variables used by this account. Even though this is a redirect, do not store the redirected url since if the account makes any changes it will redirect to a new url. Needs no authentication.

    https://canvas.instructure.com/doc/api/brand_configs.html#method.brand_configs_api.show
    """
    method = 'GET'
    url = '/api/v1/brand_variables'
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return data
