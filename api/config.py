import os
from supertokens_python.recipe import emailpassword, session, dashboard
from supertokens_python import (
    InputAppInfo,
    SupertokensConfig,
)

# this is the location of the SuperTokens core.
supertokens_config = SupertokensConfig(
    connection_uri=os.getenv("SUPERTOKENS_CONNECTION_URI"),)

app_info = InputAppInfo(
    app_name=os.getenv("APP_NAME"),
    api_domain=os.getenv("BACKEND_URI"),
    website_domain=os.getenv("FRONTEND_URI"),
)

framework = "flask"

# recipeList contains all the modules that you want to
# use from SuperTokens. See the full list here: https://supertokens.com/docs/guides
recipe_list = [
    session.init(),
    emailpassword.init(),
    dashboard.init(),
]
