# 1ta ozgaruvchida 2 ta narsani birlashtirish imkonini beradi
from typing import Annotated
from datetime import datetime
from decimal import Decimal
from sqlalchemy.orm import mapped_column
from sqlalchemy import Text, text


# ORM python class objectlarini ishlatgani uchun juda yaxshi
# va kotta projectlarda syntax boyicha va code tushunish boyicha va
# soddaligi boyicha juda zor

# Core Bu OOP emas bu sqlga eng yaqin usul sql table orqali qilinadi


# For Example

# ORM
# (user degan object bor, u bir odamni bildiradi)
# user = User(name="Ali")
# session.add(user)

# hudi shu core
# stmt = users.insert().values('Ali')
# conn.execute(stmt)

# primary_key custom
intpk = Annotated[int, mapped_column(primary_key=True)]
# bu 30 va 50 stringlar
str_30 = Annotated[str, 30]
str_50 = Annotated[str, 50]
# ORM uni avtomatik chaqirmaydi
full_text = Annotated[str, mapped_column(Text, deferred=True)]
#yaratilgan vaqt 
created_at = Annotated[
    datetime,
    mapped_column(server_default=text('TIMEZONE(utc,now())'))
]
#ozgargan vaqt
updated_at = Annotated[
    datetime,
    mapped_column(
        server_default=text('TIMEZONE(utc,now())'),
        onupdate=datetime.utcnow
    )
]