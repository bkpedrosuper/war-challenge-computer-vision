import os

from dotenv import dotenv_values

config = {
    **dotenv_values(".shared.env"),  # load shared development variables
    **dotenv_values(".env.secret"),  # load sensitive variables
    **os.environ,  # override loaded values with environment variables
}

DEV_ENV = "dev"

is_dev = config.get("ENVIRONMENT", DEV_ENV) == DEV_ENV
is_prod = not is_dev
