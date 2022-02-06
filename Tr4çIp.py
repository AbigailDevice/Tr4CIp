import pygeoip

GeIp = pygeoip​.​GeoIP​(​'GeoLiteCity.dat'​) 
​res​ ​=​ ​gip​.​record_by_addr​(​input(" ##Enter Ip: ")​)
 
​for​ ​key​,​val​ ​in​ ​res​.​items​(): 
 ​        ​print​(​'%s : %s'​ ​%​ (​key​,​val​))