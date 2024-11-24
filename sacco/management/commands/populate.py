from django.core.management import BaseCommand

from sacco.models import Customer


class Command(BaseCommand):
  def handle(self, *args, **options):
    customers=[
    {
        "first_name": "Malina",
        "last_name": "Gwennie",
        "email": "gcusty0@twitter.com",
        "gender": "Female",
        "weight": 46.46,
        "dob": "2021-07-10"
    },
    {
        "first_name": "Blake",
        "last_name": "Reagen",
        "email": "rechalie1@barnesandnoble.com",
        "gender": "Male",
        "weight": 31.85,
        "dob": "2021-02-16"
    },
    {
        "first_name": "Silvanus",
        "last_name": "Palm",
        "email": "pmathey2@constantcontact.com",
        "gender": "Male",
        "weight": 38.35,
        "dob": "2014-12-02"
    },
    {
        "first_name": "Blair",
        "last_name": "Sally",
        "email": "slunk3@rediff.com",
        "gender": "Female",
        "weight": 30.57,
        "dob": "2019-11-24"
    },
    {
        "first_name": "Marya",
        "last_name": "Carleen",
        "email": "csimoneschi4@com.com",
        "gender": "Female",
        "weight": 30.26,
        "dob": "2020-12-28"
    },
    {
        "first_name": "Marsiella",
        "last_name": "Francoise",
        "email": "fbernardoni5@seesaa.net",
        "gender": "Female",
        "weight": 47.28,
        "dob": "2018-07-25"
    },
    {
        "first_name": "Camile",
        "last_name": "Linzy",
        "email": "lmeere6@reuters.com",
        "gender": "Female",
        "weight": 43.57,
        "dob": "2015-08-20"
    },
    {
        "first_name": "Hi",
        "last_name": "Hashim",
        "email": "hgraalmans7@360.cn",
        "gender": "Male",
        "weight": 43.96,
        "dob": "2014-12-25"
    },
    {
        "first_name": "Cesya",
        "last_name": "Sidonia",
        "email": "stookill8@dagondesign.com",
        "gender": "Female",
        "weight": 41.71,
        "dob": "2017-07-01"
    },
    {
        "first_name": "Kristian",
        "last_name": "Alastair",
        "email": "abartosek9@goo.ne.jp",
        "gender": "Male",
        "weight": 32.98,
        "dob": "2019-05-30"
    },
    {
        "first_name": "Deny",
        "last_name": "Cyb",
        "email": "ceppa@webs.com",
        "gender": "Female",
        "weight": 30.47,
        "dob": "2015-03-07"
    },
    {
        "first_name": "Lulita",
        "last_name": "Cordelia",
        "email": "cmacfadinb@creativecommons.org",
        "gender": "Female",
        "weight": 35.7,
        "dob": "2020-02-10"
    },
    {
        "first_name": "Sheilah",
        "last_name": "Iseabal",
        "email": "ibigriggc@vk.com",
        "gender": "Female",
        "weight": 31.48,
        "dob": "2021-12-11"
    }
    ]
    for c in customers:
       customer= Customer(**c)
       customer.save()


       print('Populated Customers Successfully')