#this module use amap api to get all the factories of beichen discrit of tianjin  
#thanks to amap company. please visit http://ditu.amap.com/ to get more information  
  
#coding:utf-8  
  
import urllib  
import xml.dom.minidom as minidom  
import string  
  
file_name='result.txt'                 #write result to this file  
url_amap=r'http://restapi.amap.com/v3/place/text?&keyword=&types=170300&city=120113&citylimit=true&&output=xml&offset=20&page=1&key=08ffdae193c55c7c3268587884f2d1da&extensions=base'  
facility_type=r'types=170300'       #factory facilities  
region=r'city=025'               #beichen of tianjin  
each_page_rec=20                    #results that displays in one page  
which_pach=r'page=1'                #display which page  
xml_file='tmp.xml'                  #xml filen name  
  
#write logs  
def log2file(file_handle,text_info):  
    file_handle.write(text_info)  
  
#get html by url and save the data to xml file  
def getHtml(url):  
    page = urllib.urlopen(url)  
    html = page.read()  
  
    try:   
        #open xml file and save data to it  
        with open(xml_file,'w') as xml_file_handle:  
            xml_file_handle.write(html)  
    except IOError as err:  
        print "IO error: "+str(err)  
        return -1  
  
    return 0  
  
#phrase data from xml  
def parseXML():  
    total_rec=1                      #record number  
      
    #open xml file and get data record  
    try:  
        with open(file_name,'a') as file_handle:  
            dom = minidom.parse(xml_file)  
            root = dom.getElementsByTagName("response") #The function getElementsByTagName returns NodeList.  
  
            for node in root:  
                total_rec=node.getElementsByTagName('count')[0].childNodes[0].nodeValue  
                  
                pois = node.getElementsByTagName("pois")  
                for poi in pois[0].getElementsByTagName('poi'):  
                    name=poi.getElementsByTagName("name")[0].childNodes[0].nodeValue  
                    location=poi.getElementsByTagName("location")[0].childNodes[0].nodeValue  
                    text_info=''+name+','+location+'\n'  
                    print text_info  
                    #save data record  
                    log2file(file_handle,text_info.encode('utf-8'))  
                  
    except IOError as err:  
        print "IO error: "+str(err)  
  
    return total_rec  
if __name__=='__main__':  
    if getHtml(url_amap)==0:  
        print 'parsing page 1 ... ...'  
        #parse the xml file and get the total record number  
        total_record_str=parseXML()  
  
        total_record=string.atoi(str(total_record_str))  
        if (total_record%each_page_rec)!=0:  
            page_number=total_record/each_page_rec+2  
        else:  
            page_number=total_record/each_page_rec+1  
  
        #retrive the other records  
        for each_page in range(2,page_number):  
            print 'parsing page '+str(each_page)+' ... ...'  
            url_amap=url_amap.replace('page='+str(each_page-1),'page='+str(each_page))  
            getHtml(url_amap)  
            parseXML()  
  
    else:  
        print 'error: fail to get xml from amap'  
          
      