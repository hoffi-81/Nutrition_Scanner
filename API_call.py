import requests
# from test import bar_code_int


def get_data(int_bar_code):
     url = "https://world.openfoodfacts.org/api/v3/product/{}.json".format(4061462341151) #int_bar_code

     json_raw = requests.request(method="get", url=url).json()

     needed_info = {"product":["product_name_de","brands",{"nutriments":["carbohydrates","carbohydrates_100g","carbohydrates_unit","carbohydrates_value","energy","energy-kcal","energy-kcal_100g","energy-kcal_unit","energy-kcal_value","energy-kcal_value_computed","energy-kj","energy-kj_100g","energy-kj_unit","energy-kj_value","energy-kj_value_computed","energy_100g","energy_unit","energy_value","fat","fat_100g","fat_unit","fat_value","fruits-vegetables-legumes-estimate-from-ingredients_100g","fruits-vegetables-legumes-estimate-from-ingredients_serving","fruits-vegetables-nuts-estimate-from-ingredients_100g","fruits-vegetables-nuts-estimate-from-ingredients_serving","nova-group","nova-group_100g","nova-group_serving","nutrition-score-fr","nutrition-score-fr_100g","proteins","proteins_100g","proteins_unit","proteins_value","salt","salt_100g","salt_unit","salt_value","saturated-fat","saturated-fat_100g","saturated-fat_unit","saturated-fat_value","sodium","sodium_100g","sodium_unit","sodium_value","sugars","sugars_100g","sugars_unit","sugars_value"]}]}

     return_json_data = {}

     for key, values in needed_info.items():
          return_json_data[key] = {}
          for value in values:
               try:
                    # print(json_raw[key][value])
                    return_json_data[key][value] = json_raw[key][value]
               except:
                    for subkey, sub_value_list in value.items():
                         for sub_value in sub_value_list:
                              if subkey not in return_json_data[key]:
                                   return_json_data[key][subkey] = {}
                              return_json_data[key][subkey][sub_value] = json_raw[key][subkey][sub_value]

     return return_json_data


if __name__ == "__main__":
     print(get_data(2))
                              
