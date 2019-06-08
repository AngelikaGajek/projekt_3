from kivy.garden.mapview import MapMarker
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from random import shuffle
global points_all, counts
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.lang import Builder 
from kivy.garden.mapview import MapView



points_all = list_of_points = [
                ['warszawa.jpg', 52.2297700, 21.0117800],
                ['wenecja.jpg', 45.4371300, 12.3326500],
                ['Giza.jpg', 30.0080800, 31.2109300],
                ['londyn.jpg', 51.5085300, -0.1257400],
                ['rzym.jpeg', 41.8919300, 12.5113300],
                ['barcelona.jpg', 41.3887900, 2.1589900],
                ['oslo.jpg', 59.9127300, 10.7460900],
                ['tokio.jpg', 35.6895000, 139.6917100],
                ['moskwa.jpg', 55.7522200, 37.6155600],
                ['rio.jpg', -22.9027800, -43.2075000],
                ]
shuffle(points_all)
counts=len(points_all)
class Form(BoxLayout):   
    def draw_marker(self):
        try:
            self.my_map.remove_marker(self.marker)
        except:
            pass
        
        self.latitude = self.my_map.lat
        self.longitude = self.my_map.lon
        
        self.marker = MapMarker(lat=self.latitude, lon=self.longitude)
        self.my_map.add_marker(self.marker)
        
        self.search_lat.text = "{}".format(self.latitude)
        self.search_long.text = "{}".format(self.longitude)
        
    def check_points(self):
        r=10
        if self.my_image.source in ['warszawa.jpg']:
            pass
        else:
            if (self.latitude-self.curr_img[1])**2 + (self.longitude -self.curr_img[2])**2 <= r**2:
                self.my_score.text=str(int(self.my_score.text)+1)
    def next_img(self):
        #self.my_button_check.enabled = True
        if len(points_all)>=1:
            self.curr_img=points_all.pop()
            self.my_image.source = self.curr_img[0]
        else:
            self.my_button_next.text="Zakończ"
            


class MapViewApp(App):
    pass

MapViewApp().run()