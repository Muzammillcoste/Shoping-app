from abc import ABCMeta, abstractmethod
from kivy.lang.builder import Builder
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.textfield import TextInput, TextfieldLabel
from kivymd.uix.boxlayout import MDBoxLayout

class GUI:
    '''Class GUI having multiple inside multiple classes'''

    class Content(MDBoxLayout):
        pass

    # Following are the windows classes inherit.

    class SignupWindow(Screen):
        ''' class signup_window'''

        def Submit_signup_func(self, name, email, password, phone_number):
            User_Signup(name, email, password, phone_number).Save_Info()

    class LoginWindow(Screen):
        '''class login_window'''

        def Log_in_func(self, email, password):
            '''log_in_func method, inside the class login window.'''
            with open('sign_up_data.txt') as g:
                '''Opening file having sign_up_data'''
                old = eval(g.read())
                for i in range(len(old)):
                    if email == old[i][2] and password == old[i][3]:
                        return True
                else:
                    return False

    class MainWindow(Screen):
        '''class  main _window.'''
        pass

    class GrossWindow(Screen):
        '''class Gross_window.'''
        pass

    class ElectWindow(Screen):
        '''class Electronic_window.'''
        pass

    class FashionWindow(Screen):
        '''class Fashion_window.'''
        pass

    class PaymentWindow(Screen):
        '''class payment_window.'''

        def Payment_func(self, name):
            try:
                with open("cart_data.txt") as f:
                    data = eval(f.read())

                with open('sign_up_data.txt') as g:
                    old = eval(g.read())
                    for i in range(len(old)):
                        if name == old[i][1]:
                            old[i].append(data)

                with open("sign_up_data.txt", "w") as h:
                    h.write(str(old))
                    Cart().cart_product()
                return True
            except None:
                return False

    class ScreenManager(ScreenManager):
        '''class Screen_manager'''
        pass

    # KivyMD is an extension of the Kivy framework. KivyMD is a collection of Material Design widgets for use with Kivy.

    class OOP_project(MDApp):
        '''class oop_project'''

        # Following are the method of the class oop_project.

        def build(self):
            '''method: build, inside class oop_project.'''
            self.theme_cls.theme_style = 'Dark'
            self.theme_cls.primary_palette = 'Cyan'

        def Account_Info(self, email, password):
            '''method: Account_info, inside class oop_project.'''
            with open("sign_up_data.txt") as f:
                '''Opening the sign_up_data file, inside the method Account_info '''
                list = eval(f.read())
                for i in range(len(list)):
                    if email == list[i][2] and password == list[i][3]:
                        info = f"Name:{list[i][1]}\nEmail:{list[i][2]}\nPassword:{list[i][3]}\nPhone:{list[i][4]}"
                        return info
                else:
                    return "Please enter valid email and password"

        def main_menu_dialog(self, email, password):
            '''method: main_menu_dialog, inside class oop_project.'''
            self.dialog = MDDialog(title='Account Details',
                                   text=str(self.Account_Info(email, password)), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)]
                                   )
            self.dialog.open()

        def navigation_draw(self):
            '''method: navigation_draw, inside class oop_project.'''
            self.dialog = MDDialog(title='Cart ',
                                   text=Cart().show_product() + '\n\nYour total bill is ' + str(
                                       Payment().calculate_bill()), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)]
                                   )
            self.dialog.open()

        def close_dialog(self, obj):
            '''method: close_dialog, inside class oop_project.'''
            self.dialog.dismiss()

        def remove(self, id):
            '''method: remove, inside class oop_project.'''
            Cart().remove_product(str(Category().get_grossery(id)))

        def add(self, id):
            '''method: add, inside class oop_project.'''
            Cart().add_product(str(Category().get_grossery(id)))

        def add_to_cart_egg(self):
            '''method: add_to_cart_egg, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_grossery('1')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart', on_release=lambda x: self.add('1')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove('1'))]
                                   )
            self.dialog.open()

        def add_to_cart_fish(self):
            '''method: add_to cart_fish, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_grossery('2')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart', on_release=lambda x: self.add('2')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove('2'))]
                                   )
            self.dialog.open()

        def add_to_cart_beef(self):
            '''method: add_to cart_beef, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_grossery('3')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart', on_release=lambda x: self.add('3')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove('3'))]
                                   )
            self.dialog.open()

        def add_to_cart_flour(self):
            '''method: add_to cart_flour, inside class oop_project.'''
            content_box = Builder.load_string(content)
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_grossery('4')), size_hint=(0.8, 1),
                                   content_cls=GUI.Content(),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart', on_release=lambda x: self.add('4')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove('4'))]
                                   )
            self.dialog.open()

        def add_to_cart_milk(self):
            '''method: add_to cart_milk, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_grossery('5')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart', on_release=lambda x: self.add('5')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove('5'))]
                                   )
            self.dialog.open()

        def add_to_cart_bread(self):
            '''method: add_to cart_bread, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_grossery('6')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart', on_release=lambda x: self.add('6')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove('6'))]
                                   )
            self.dialog.open()

        def add_to_cart_oil(self):
            '''method: add_to cart_oil, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_grossery('7')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart', on_release=lambda x: self.add('7')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove('7'))]
                                   )
            self.dialog.open()

        def add_to_cart_sugar(self):
            '''method: add_to cart_sugar, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_grossery('8')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart', on_release=lambda x: self.add('8')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove('8'))]
                                   )
            self.dialog.open()

        def add_to_cart_salt(self):
            '''method: add_to cart_salt, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_grossery('9')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart', on_release=lambda x: self.add('9')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove('9'))]
                                   )
            self.dialog.open()

        def add_to_cart_butter(self):
            '''method: add_to cart_butter, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_grossery('10')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart', on_release=lambda x: self.add('10')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove('10'))]
                                   )
            self.dialog.open()

        def remove_fashion(self, id):
            '''method: remove_fashion, inside class oop_project.'''
            Cart().remove_product(str(Category().get_fashion(id)))

        def add_fashion(self, id):
            '''method for add_fashion, inside class oop_project.'''
            Cart().add_product(str(Category().get_fashion(id)))

        def add_to_cart_body(self):
            '''method: add_to cart_body, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_fashion('1')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart',
                                                         on_release=lambda x: self.add_fashion('1')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove_fashion('1'))]
                                   )
            self.dialog.open()

        def add_to_cart_face(self):
            '''method: add_to cart_face, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_fashion('2')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart',
                                                         on_release=lambda x: self.add_fashion('2')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove_fashion('2'))]
                                   )
            self.dialog.open()

        def add_to_cart_hair(self):
            '''method: add_to cart_hair, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_fashion('3')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart',
                                                         on_release=lambda x: self.add_fashion('3')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove_fashion('3'))]
                                   )
            self.dialog.open()

        def add_to_cart_lip(self):
            '''method: add_to cart_lipstick, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_fashion('4')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart',
                                                         on_release=lambda x: self.add_fashion('4')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove_fashion('4'))]
                                   )
            self.dialog.open()

        def add_to_cart_pant(self):
            '''method: add_to cart_pant, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_fashion('5')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart',
                                                         on_release=lambda x: self.add_fashion('5')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove_fashion('5'))]
                                   )
            self.dialog.open()

        def add_to_cart_perfume(self):
            '''method: add_to cart_perfume, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_fashion('6')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart',
                                                         on_release=lambda x: self.add_fashion('6')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove_fashion('6'))]
                                   )
            self.dialog.open()

        def add_to_cart_shirt(self):
            '''method: add_to cart_shirt, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_fashion('7')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart',
                                                         on_release=lambda x: self.add_fashion('7')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove_fashion('7'))]
                                   )
            self.dialog.open()

        def add_to_cart_shoes(self):
            '''method: add_to cart_shoes, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_fashion('8')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart',
                                                         on_release=lambda x: self.add_fashion('8')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove_fashion('8'))]
                                   )
            self.dialog.open()

        def add_to_cart_watch(self):
            '''method: add_to cart_watch, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_fashion('9')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart',
                                                         on_release=lambda x: self.add_fashion('9')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove_fashion('9'))]
                                   )
            self.dialog.open()

        def add_to_cart_cap(self):
            '''method: add_to cart_cap, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_fashion('10')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart',
                                                         on_release=lambda x: self.add_fashion('10')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove_fashion('10'))]
                                   )
            self.dialog.open()

        def remove_elctronics(self, id):
            '''method: remove_fashion, inside class oop_project.'''
            Cart().remove_product(str(Category().get_electronics(id)))

        def add_electronics(self, id):
            '''method: add_fashion, inside class oop_project.'''
            Cart().add_product(str(Category().get_electronics(id)))

        def add_to_cart_mac(self):
            '''method: add_to cart_mac, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_electronics('1')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart',
                                                         on_release=lambda x: self.add_electronics('1')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove_elctronics('1'))]
                                   )
            self.dialog.open()

        def add_to_cart_bulb(self):
            '''method: add_to cart_bulb, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_electronics('2')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart',
                                                         on_release=lambda x: self.add_electronics('2')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove_elctronics('2'))]
                                   )
            self.dialog.open()

        def add_to_cart_fan(self):
            '''method: add_to cart_fan, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_electronics('3')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart',
                                                         on_release=lambda x: self.add_electronics('3')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove_elctronics('3'))]
                                   )
            self.dialog.open()

        def add_to_cart_fridge(self):
            '''method: add_to cart_fridge, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_electronics('4')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart',
                                                         on_release=lambda x: self.add_electronics('4')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove_elctronics('4'))]
                                   )
            self.dialog.open()

        def add_to_cart_iphone(self):
            '''method: add_to cart_iphone, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_electronics('5')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart',
                                                         on_release=lambda x: self.add_electronics('5')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove_elctronics('5'))]
                                   )
            self.dialog.open()

        def add_to_cart_led(self):
            '''method: add_to cart_LED, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_electronics('6')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart',
                                                         on_release=lambda x: self.add_electronics('6')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove_elctronics('6'))]
                                   )
            self.dialog.open()

        def add_to_cart_oven(self):
            '''method: add_to cart_oven, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_electronics('7')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart',
                                                         on_release=lambda x: self.add_electronics('7')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove_elctronics('7'))]
                                   )
            self.dialog.open()

        def add_to_cart_samsung(self):
            '''method: add_to cart_samsung, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_electronics('8')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart',
                                                         on_release=lambda x: self.add_electronics('8')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove_elctronics('8'))]
                                   )
            self.dialog.open()

        def add_to_cart_wash_machine(self):
            '''method: add_to cart_washing machine, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_electronics('9')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart',
                                                         on_release=lambda x: self.add_electronics('9')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove_elctronics('9'))]
                                   )
            self.dialog.open()

        def add_to_cart_air(self):
            '''method:  add_to cart_air, inside class oop_project.'''
            self.dialog = MDDialog(title="Place your order",
                                   text=str(Category().get_electronics('10')), size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Add to cart',
                                                         on_release=lambda x: self.add_electronics('10')),
                                            MDFlatButton(text='Remove from cart',
                                                         on_release=lambda x: self.remove_elctronics('10'))]
                                   )
            self.dialog.open()

        def menu_dialog(self):
            '''method: menu_dialog, inside class oop_project.'''
            self.dialog = MDDialog(title='Menu',
                                   text="where you have to go?", size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='Grossary'),
                                            MDFlatButton(text='Fashion'),
                                            MDFlatButton(text='Electronics')]
                                   )
            self.dialog.open()


# back-end
class Person:
    '''Class person '''

    def __init__(self, email, password):
        '''constructor, inside class person.'''
        self.email = email
        self.password = password

    @abstractmethod
    def Get_Info(self):
        '''method: Get_info, inside class person.'''
        return self.email, self.password


class Admin(Person):
    '''class Admin,inherit from class person.'''

    def __init__(self, name, email, password):
        '''constructor, inside class Admin.'''
        super().__init__(email, password)
        self.name = name
        super().Get_Info()

    def __str__(self):
        '''method overloading for Person class'''
        return (self.name, self.email, self.password)


class User_Signup(Person):
    '''class User_signup, inherit from class person.'''

    def __init__(self, name, email, password, phone_number):
        '''constructor, inside class user_signup. '''
        super().__init__(email, password)
        self.__name = name
        self.__phone_number = phone_number

    def Save_Info(self):
        '''method: save_info,inside class user_signup'''
        with open('sign_up_data.txt') as g:
            '''Opening sign_up_data file, inside class user_signup.'''
            old = eval(g.read())
            last = len(old)
            id_no = old[last - 1][0]
            id_no += 1
            id = [id_no, self.__name, self.email, self.password, self.__phone_number]
            old.append(id)

        with open('sign_up_data.txt', 'w') as f:
            '''Opening sign_up_data file in write mode, inside class user_signup.'''
            f.write(str(old))

    def Get_Info(self):
        '''method: Get_info,inside class user_signup'''
        return (self.__name, self.email, self.password, self.__phone_number)


class Category:
    '''class Category'''

    def get_electronics(self, id):
        '''method: get_electronics, inside class Category'''
        with open('electronics.txt') as f:
            '''Opening Electronics file, inside class Category'''
            dict = eval(f.read())
            item = dict[id]
        return item

    def get_fashion(self, id):
        '''method: get_fashion, inside class Category'''
        with open('fashion.txt') as f:
            '''Opening fashion file, inside class Category'''
            dict = eval(f.read())
            item = dict[id]
        return item

    def get_grossery(self, id):
        '''method: get_grossery, inside class Category'''
        with open('grocery.txt') as f:
            '''Opening grossery file, inside class Category'''
            dict = eval(f.read())
            item = dict[id]
        return item


class Cart:
    '''class cart.'''

    def add_product(self, product):
        '''method: add_product, inside class cart.'''
        with open("cart_data.txt") as f:
            '''Opening cart_data file, inside class cart.'''
            old = eval(f.read())
            if product not in old:
                old.append(eval(product))
        with open("cart_data.txt", 'w') as g:
            '''Opening cart_data file in write mode, inside class cart.'''
            g.write(str(old))

    def remove_product(self, product):
        '''method: remove_product, inside class cart.'''
        with open("cart_data.txt") as f:
            '''Opening cart_data file, inside class cart.'''
            old = eval(f.read())
            if eval(product) in old:
                old.remove(eval(product))
        with open("cart_data.txt", 'w') as g:
            '''Opening cart_data file in write mode, inside class cart.'''
            g.write(str(old))

    def show_product(self):
        '''method: show_product, inside class cart.'''
        with open("cart_data.txt") as f:
            '''Opening cart_data file, inside class cart.'''
            return f.read()

    def cart_product(self):
        '''method: cart_product, inside class cart.'''
        with open("cart_data.txt", "w") as f:
            f.write("[]")


class Payment:
    '''class payment.'''
    bill = 0

    def calculate_bill(self):
        '''method: calculate_bill, inside class payment.'''
        with open("cart_data.txt") as f:
            '''Opening cart_data file, inside class payment.'''
            list = eval(f.read())
            for i in range(len(list)):
                self.bill += int(list[i][1])
            return self.bill

    def bill_details(self):
        '''method: bill_details, inside class payment.'''
        pass

    def payment_method(self):
        '''method: payment_method, inside class payment.'''
        pass

    def feedback(self):
        '''method: feedback, inside class payment.'''
        pass


# Driver code
GUI().OOP_project().run()
