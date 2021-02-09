## From the Build a SaaS App with Flask course
by Nick Janetakis

[https://nickjanetakis.com/blog/dockerize-a-flask-celery-and-redis-application-with-docker-compose](https://nickjanetakis.com/blog/dockerize-a-flask-celery-and-redis-application-with-docker-compose)
[https://buildasaasappwithflask.com](https://buildasaasappwithflask.com/)

I just stripped out anything that wasn't related to getting celery working.

Then I added celery beat for periodic tasks (cron jobs).
[https://blog.miguelgrinberg.com/post/using-celery-with-flask](https://blog.miguelgrinberg.com/post/using-celery-with-flask)
[https://blog.miguelgrinberg.com/post/run-your-flask-regularly-scheduled-jobs-with-cron](https://blog.miguelgrinberg.com/post/run-your-flask-regularly-scheduled-jobs-with-cron)

Also thanks to Chris Samiullah from [CourseMaker](https://coursemaker.org/) who helped by sharing an illustrative example of how it worked for him in an old project: [https://gist.github.com/ChristopherGS/baa74b96b35a326f938ceb7c93d24a82](https://gist.github.com/ChristopherGS/baa74b96b35a326f938ceb7c93d24a82)

Next I want to get Flower implemented to monitor it:
[https://flower.readthedocs.io/en/latest/](https://flower.readthedocs.io/en/latest/)