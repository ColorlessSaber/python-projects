"""
Demonstration of denoting a protected and private attribute and function
"""

class PrivateVault:
    def __init__(self):
        self._combination = 24587

    def __change_combination(self, new_combination):
        """
        Change the vault combination lock
        """
        self._combination = new_combination

    def request_combination_change(self, access_key, new_combination_request):
        """
        Vault owner is able to change the combination if they have the acces key from
        the manufacture
        """
        if access_key == 'FXVT748P':
            self.__change_combination(new_combination_request)
            print('combination successfully changed')
        else:
            print("access not granted")

if __name__ == '__main__':
    my_vault = PrivateVault()
    my_vault.request_combination_change('FXVT748P', 57893)