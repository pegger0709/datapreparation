import pandas as pd
import CountryManager

class AustriaManager():

    BASE_URL_AUSTRIA = "https://opendata.arcgis.com/datasets/123014e4ac74408b970dd1eb060f9cf0_4.csv"

    def download(self):
        self.aut = pd.read_csv(self.BASE_URL_AUSTRIA, sep=",")
        return self

    def get_raw_data(self) -> pd.DataFrame:
        '''

        :return: the raw data dataframe
        '''
        self.aut.to_csv("austria.csv", encoding="utf-8-sig", index=False)
        return self.aut

    def harmonized(self) -> pd.DataFrame:
        '''

        :return: the harmonized dataframe
        '''
        self.aut2 = self.aut.drop(["OBJECTID", "infizierte_pro_ew", "zuwachs", "zuwachs_prozent", "einwohner"], axis=1)
        colnames = ["region_small_code_native", "region_small_name", "region_large_code_native", "region_large_name",
                   "no_cases", "Shape_Length", "Shape_Area", "report_date"]
        self.aut2.columns = colnames

        self.aut2["uuid"] = ""
        self.aut2["source"] = "Austria"
        self.aut2["country_name"] = "Austria"
        self.aut2["country_iso"] = "AUT"

        self.aut2 = self.aut2[["uuid", "source", "report_date", "country_name", "country_iso", "region_large_name", "region_large_code_native",

                    "region_small_name", "region_small_code_native", "Shape_Length", "Shape_Area", "no_cases"]]
        self.aut2.to_csv("austria_harmonized.csv", encoding="utf-8-sig", index=False)
        return self.aut2


if __name__ == '__main__':

    cm = AustriaManager()

    #cm.download().harmonized()
    #cm.download()
    #cm.get_raw_data()

    #cm.harmonized()
