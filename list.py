from flet import *
from wf import Wifi

class List(UserControl):
    def __init__(self,page):
        self.page=page
        super().__init__()
    
    def build(self):
        ps=Wifi.getPs(self)
        containers=[]
        for nom, values in ps.items():
            code = values["psk"]
            cont=Container(
                    Text(f"{nom} ---> {code}",width=500),
                    bgcolor=colors.GREEN_600,
                    width=500,
                    height=50,
                    border_radius=10,
                    alignment=alignment.center, 
                    padding=padding.only(left=50),
                    margin=margin.only(left=30,right=30)
                )
            containers.append(cont)
        
        c=Column(
            controls=containers
            
        )
        return c