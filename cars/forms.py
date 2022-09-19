from django import forms
from .models import Cars

#Form For Adding Item


class CarAddForm(forms.ModelForm):
    class Meta:
        model = Cars

        #manufacture_date = forms.TypedChoiceField(coerce=int, choices=year_choices, initial=current_year)
        #manufacture_date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
        fields = ['make', 'car_name','price','mileage','drive','transmission','fueltype','color', 'engine', 'body_type','airbag', 'navigation', 'cd','leather_seat','ac','fog_light',
        'rear_spoiler','back_camera',
        'alloy_wheels','power_window','power_steering','keyless_entry','spare_tyre','sunroof','AntilockBrakingSystem','radio','tv',
        'car_main_image','car_sub_image1','car_sub_image2','car_sub_image3','car_sub_image4','car_sub_image5','car_sub_image6','car_sub_image7','car_sub_image8','car_sub_image9',
        'car_sub_image10']

        # widgets = {
        #     'manufacture_date': DateInput(),
        # }
    def clean_make(self):

        make = self.cleaned_data.get('make')
        if not make:
            raise forms.ValidationError('You must fill this field')
        return make

    def clean_car_name(self):

        car_name = self.cleaned_data.get('car_name')
        if not car_name:
            raise forms.ValidationError('You must fill this field')
        return car_name

    def clean_price(self):

        price = self.cleaned_data.get('price')
        if not price:
            raise forms.ValidationError('You must fill this field')
        return price

    def clean_mileage(self):
        mileage = self.cleaned_data.get('mileage')
        if not mileage:
            raise forms.ValidationError('You must fill this field')
        return mileage

    def clean_drive(self):
        drive = self.cleaned_data.get('drive')
        if not drive:
            raise forms.ValidationError('You must fill this field')
        return drive

    def clean_transmission(self):

        transmission = self.cleaned_data.get('transmission')
        if not transmission:
            raise forms.ValidationError('You must fill this field')
        return transmission

    def clean_fueltype(self):
        fueltype = self.cleaned_data.get('fueltype')
        if not fueltype:
            raise forms.ValidationError('You must fill this field')
        return fueltype

    def clean_color(self):

        color = self.cleaned_data.get('color')
        if not color:
            raise forms.ValidationError('You must fill this field')
        return color


    def clean_engine(self):
        engine = self.cleaned_data.get('engine')
        if not engine:
            raise forms.ValidationError('You must fill this field')
        return engine

    def clean_body_type(self):
        body_type = self.cleaned_data.get('body_type')
        if not body_type:
            raise forms.ValidationError('You must fill this field')
        return body_type

    def clean_airbag(self):

        airbag = self.cleaned_data.get('airbag')
        if not airbag:
            raise forms.ValidationError('You must fill this field')
        return airbag

    def clean_navigation(self):
        navigation = self.cleaned_data.get('navigation')
        if not navigation:
            raise forms.ValidationError('You must fill this field')
        return navigation

    def clean_cd(self):
        cd = self.cleaned_data.get('cd')
        if not cd:
            raise forms.ValidationError('You must fill this field')
        return cd
    def clean_leather_seat(self):

        leather_seat = self.cleaned_data.get('leather_seat')
        if not leather_seat:
            raise forms.ValidationError('You must fill this field')
        return leather_seat

    def clean_ac(self):
        ac = self.cleaned_data.get('ac')
        if not ac:
            raise forms.ValidationError('You must fill this field')
        return ac

    def clean_fog_light(self):

        fog_light = self.cleaned_data.get('fog_light')
        if not fog_light:
            raise forms.ValidationError('You must fill this field')
        return fog_light

    def clean_rear_spoiler(self):
        rear_spoiler = self.cleaned_data.get('rear_spoiler')
        if not rear_spoiler:
            raise forms.ValidationError('You must fill this field')
        return rear_spoiler

    def clean_back_camera(self):
        back_camera = self.cleaned_data.get('back_camera')
        if not back_camera:
            raise forms.ValidationError('You must fill this field')
        return back_camera

    def clean_alloy_wheels(self):

        alloy_wheels = self.cleaned_data.get('alloy_wheels')
        if not alloy_wheels:
            raise forms.ValidationError('You must fill this field')
        return alloy_wheels

    def clean_power_window(self):

        power_window = self.cleaned_data.get('power_window')
        if not power_window:
            raise forms.ValidationError('You must fill this field')
        return power_window

    def clean_keyless_entry(self):

        keyless_entry = self.cleaned_data.get('keyless_entry')
        if not keyless_entry:
            raise forms.ValidationError('You must fill this field')
        return keyless_entry

    def clean_spare_tyre(self):

        spare_tyre = self.cleaned_data.get('spare_tyre')
        if not spare_tyre:
            raise forms.ValidationError('You must fill this field')
        return spare_tyre
    def clean_sunroof(self):

        sunroof = self.cleaned_data.get('sunroof')
        if not sunroof:
            raise forms.ValidationError('You must fill this field')
        return sunroof
    def clean_AntilockBrakingSystem(self):

        AntilockBrakingSystem = self.cleaned_data.get('AntilockBrakingSystem')
        if not AntilockBrakingSystem:
            raise forms.ValidationError('You must fill this field')
        return AntilockBrakingSystem


    def clean_radio(self):

        radio = self.cleaned_data.get('radio')
        if not radio:
            raise forms.ValidationError('You must fill this field')
        return radio

    def clean_tv(self):

        tv = self.cleaned_data.get('tv')
        if not tv:
            raise forms.ValidationError('You must fill this field')
        return tv
        
    def clean_car_main_image(self):
        car_main_image = self.cleaned_data.get('car_main_image')
        if not car_main_image:
            raise forms.ValidationError('You must fill this field')
        return car_main_image

    def clean_car_sub_image1(self):

        car_sub_image1 = self.cleaned_data.get('car_sub_image1')
        if not car_sub_image1:
            raise forms.ValidationError('You must fill this field')
        return car_sub_image1

    def clean_car_sub_image2(self):

        car_sub_image2 = self.cleaned_data.get('car_sub_image2')
        if not car_sub_image2:
            raise forms.ValidationError('You must fill this field')
        return car_sub_image2

    def clean_car_sub_image3(self):

        car_sub_image3 = self.cleaned_data.get('car_sub_image3')
        if not car_sub_image3:
            raise forms.ValidationError('You must fill this field')
        return car_sub_image3

    def clean_car_sub_image4(self):
        car_sub_image4 = self.cleaned_data.get('car_sub_image4')
        if not car_sub_image4:
            raise forms.ValidationError('You must fill this field')
        return car_sub_image4

    def clean_car_sub_image5(self):

        car_sub_image5 = self.cleaned_data.get('car_sub_image5')
        if not car_sub_image5:
            raise forms.ValidationError('You must fill this field')
        return car_sub_image5

    def clean_car_sub_image6(self):
        car_sub_image6 = self.cleaned_data.get('car_sub_image6')
        if not car_sub_image6:
            raise forms.ValidationError('You must fill this field')
        return car_sub_image6



    def clean_car_sub_image7(self):

        car_sub_image7 = self.cleaned_data.get('car_sub_image7')
        if not car_sub_image7:
            raise forms.ValidationError('You must fill this field')
        return car_sub_image7

    def clean_car_sub_image8(self):
        car_sub_image8 = self.cleaned_data.get('car_sub_image8')
        if not car_sub_image8:
            raise forms.ValidationError('You must fill this field')
        return car_sub_image8

    def clean_car_sub_image9(self):
        car_sub_image9 = self.cleaned_data.get('car_sub_image9')
        if not car_sub_image9:
            raise forms.ValidationError('You must fill this field')
        return car_sub_image9

    def clean_car_sub_image10(self):
        car_sub_image10 = self.cleaned_data.get('car_sub_image10')
        if not car_sub_image10:
            raise forms.ValidationError('You must fill this field')
        return car_sub_image10





class SearchForm(forms.ModelForm):
    class Meta:
        model = Cars
        #manufacture_date = forms.TypedChoiceField(coerce=int, choices=year_choices, initial=current_year)
        #manufacture_date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
        fields = ['car_name', 'make']
        # widgets = {
        #     'manufacture_date': DateInput(),
        # }
    # def clean_department(self):

    #     department = self.cleaned_data.get('department')
    #     if not department:
    #         raise forms.ValidationError('You must fill this field')
    # #     for instance in Inventory.objects.all():

    # #         if instance.item_name == item_name:
    # #             raise forms.ValidationError(str(item_name) + ' is already created')

    #     return department