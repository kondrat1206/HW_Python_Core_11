from collections import UserDict


class AddressBook(UserDict):

    def __init__(self):

        self.data = {}


    def is_contact_exist(self, record):

        keys = []
        for key in self.data.keys():
            keys.append(key)
        if record.name.value in keys:
            result = True
        else:
            result = False
            
        return result
    

    def is_phone_exist(self, record):

        num_values = []
        for  i in self.data[record.name.value].phones:
            num_values.append(i.value)
        if record.phones[0].value in num_values:
            result = True
        else:
            result = False

        return result


        

    def add_record(self, record):

        if len(record.phones) < 1:
            if self.is_contact_exist(record) == False:
                self.record = record
                self.data[self.record.name.value] = self.record
                result = f"Contact \"{record.name.value}\" added to address book without phone\n"
            else:
                result = f"Contact \"{record.name.value}\" already exists in address book\n"
        else:
            if self.is_contact_exist(record) == False:
                self.record = record
                self.data[self.record.name.value] = self.record
                result = f"Contact \"{record.name.value}\" added to address book with phone \"{record.phones[0].value}\"\n"
            else:
                if self.is_phone_exist(record):
                    result = f"Phone \"{record.phones[0].value}\" already exists into the contact \"{record.name.value}\"\n"
                else:
                    self.data[self.record.name.value].add_phone(record.phones[0])
                    result = f"Added new phone \"{record.phones[0].value}\" to contact \"{record.name.value}\"\n"

        return result


class Record:

    def __init__(self, name, phone=None): 
        self.name = name
        self.phones = []
        if phone != None:
            self.phones.append(phone)

    
    def add_phone(self, phone):

        self.phones.append(phone)
        result = f'Number {phone.value} added to phone list of {self.name.value}'

        return result


    def remove_phone(self, phone):
        
        phone_num = phone.value
        for id, obj in enumerate(self.phones):
            if obj == phone:
                self.phones.pop(id)
                result = f'Number {phone_num} remuved from phone list of {self.name.value}'
                break
                
        return result
    

    def change_phone(self, old_phone, new_phone):
        phone_values = []
        for number in self.phones:
            phone_values.append(number.value)
        if old_phone.value in phone_values:
            for index, obj in enumerate(self.phones):
                if obj.value == old_phone.value:
                    self.phones[index] = new_phone
                    break
            result = f"Number \"{old_phone.value}\" changed to \"{new_phone.value}\" in phone list of \"{self.name.value}\"\n"
        else:
            result = f"Phone \"{old_phone.value}\" does not exist in the phone list of contact \"{self.name.value}\"\n"
                   
        return result

class Field:
    pass


class Name(Field):
    
    def __init__(self, value):
        self.value = value


class Phone(Field):
    
    def __init__(self, value):
        self.value = value