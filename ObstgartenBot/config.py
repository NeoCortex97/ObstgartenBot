# -*- coding: utf-8 -*-
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    bot_secret: str = Field("LEER", env="BOT_ACCESS_TOKEN")
    join_link: str = Field(None, env="BOT_JOIN_LINK")
    db_string: str = Field("sqlite://~/obstgarten.sqlite", env="DATABSE_PATH")

    class Config:
        env_file = '../.env'
        env_file_encoding = 'utf-8'
