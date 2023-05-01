from fastapi_users.authentication import CookieTransport


cookie_transport = CookieTransport(cookie_name='squads', cookie_max_age=3600)
