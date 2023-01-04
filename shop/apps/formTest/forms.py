from django import forms
import datetime


class InputForm0(forms.Form):
    name=forms.CharField(max_length=10,
                         required=True,
                         label='نام',
                         widget=forms.TextInput(attrs={'placeholder':'نام را وارد کنید'}))
    family=forms.CharField(max_length=10,
                           required=True,
                           label='نام خانوادگی',
                           widget=forms.TextInput(attrs={'placeholder':'نام خانوادگی را وارد کنید'}))
    age=forms.IntegerField(label='سن',
                           label_suffix=":",
                           widget=forms.TextInput(attrs={'placeholder':'سن را وارد کنید'}))
    is_active=forms.BooleanField(initial=True,
                                 label='وضعیت')
    avg=forms.DecimalField(max_digits=4,
                           decimal_places=2,
                           label='معدل',
                           widget=forms.TextInput(attrs={'placeholder':'معدل را وارد کنید'}))
    emial=forms.EmailField(max_length=100,
                           label='ایمیل',
                           widget=forms.TextInput(attrs={'placeholder':'ایمیل را وارد کنید'}))
    # YEAR_CHOIES=['2020','2021','2022']
    # register_date=forms.DateField(widget=forms.SelectDateWidget(years=YEAR_CHOIES),label='تاریخ ثبت نام')
    register_date=forms.DateField(initial=datetime.datetime.now,
                                  widget=forms.NumberInput(attrs={'type':'date'}),label='تاریخ ثبت نام')
    url=forms.URLField(label='آدرس اینترنتی',
                       initial='www.')
    image=forms.ImageField(label='تصویر')
    WORKING=[
        ('1','شغل آزاد'),
        ('2','کارمند'),
        ('3','بدون کار'),
    ]
    work=forms.ChoiceField(choices=WORKING,label=' وضغیت شغلی')
    PRICE=[
        ('1','زیر یک میلیون تومان'),
        ('2','بالای یک میلیون تومان تا ده میلیون تومان'),
        ('3',' بالای ده میلیون تومان'),
    ]
    price=forms.ChoiceField(widget=forms.RadioSelect,choices=PRICE,label='چقدر در ماه درآمد دارید؟')
    PLAN=[
        ('1',' صاحب خانه هستید'),
        ('2',' خودروی شخصی دارید'),
        ('3',' هیچکدام'),
    ]
    plan=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=PLAN,label='  کدام یک از این مورد ها را دارید؟ میتوانید چند انتخاب داشته باشید')
    description=forms.BooleanField(widget=forms.Textarea,label='توضیحات')
    
    
    
class InputForm1(forms.Form):
    username=forms.CharField(max_length=10,required=True,label='نام کاربری')
    password=forms.CharField(max_length=100,label='رمزعبور',widget=forms.PasswordInput)