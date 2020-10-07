from django.db import models
import datetime as dt

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True, null =True, default = "")

    def __str__(self):
        return self.first_name
    def save_editor(self):
        self.save()
    class Meta:
        ordering = ['first_name']


 #tag mode
class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name


    #Class Articles
class Article(models.Model):
    title = models.CharField(max_length =60, default='')
    post = models.TextField()
    editor = models.ForeignKey('Editor', on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date_date = today)
        return news

    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pup_date__date = date)
        return news


    def __str__(self):
        return self.title



    # Testing Save Method
    # def test_save_method(self):
    #     self.james.save_editor()
    #     editors = Editor.objects.all()
    #     self.assertTrue(len(editors) > 0)