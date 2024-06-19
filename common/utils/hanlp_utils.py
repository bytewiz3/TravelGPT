from pyhanlp import * 
 
 
def select_name(text): 
    """ 
    Extract Chinese names from a piece of text 
    """ 
    segment = HanLP.newSegment().enableNameRecognize(True) 
    result = [] 
    for term in segment.seg(text): 
        if str(term.nature) == 'nr': 
            result.append(term.word) 
    return set(result) 
 
 
def select_address(text): 
    """ 
    Extract all addresses 
    """ 
    segment = HanLP.newSegment().enablePlaceRecognize(True) 
    result = [] 
    for term in segment.seg(text): 
        if str(term.nature) == 'ns': 
            result.append(term.word) 
    return set(result) 
 
 
def select_organize(text): 
    """ 
    Recognize organization names 
    """ 
    segment = HanLP.newSegment().enableOrganizationRecognize(True) 
    result = [] 
    for term in segment.seg(text): 
        if str(term.nature) == 'ntc': 
            result.append(term.word) 
    return set(result) 
 
 
if __name__ == '__main__': 
    """ 
    Extract all addresses using HanLP 
    """ 
    # a = select_address("我想去杭州三日旅游，帮我安排时间") 
    # print(a) 
    a = select_address("当然可以，下面是一个为期三天的杭州旅游行程安排，你可以根据自己的实际情况进行微调：\n\n**第一天**：西湖景区游览 \n\n- 早上：从你所在的酒店出发，首站来到中国最有名的西湖景区，可参观苏堤春晓，探寻断桥残雪的美景，体验一番“人间烟火气，最抚凡人心”的宁静之美。\n- 中午：在湖边的餐馆享受一顿湖鲜美食。\n- 下午：游览西湖的雷峰塔和三潭印月，享受一番历史文化的熏陶。\n- 晚上：可选择在南宋御街品尝传统的杭州小吃，或者坐在湖边欣赏西湖的夜景。\n\n**第二天**：杭州市区文化历史探索\n\n- 早上：前往中国丝绸博物馆，欣赏中国古代的丝绸文化。\n- 中午：在附近的餐厅享用午餐，体验杭州的饮食文化。\n- 下午：前往宋城，体验宋朝的文化和生活方式，还可以看到精彩的演出《宋城千古情》。\n- 晚上：可选择在江南忆，品尝美食，观赏古典的江南水乡风情表演。\n\n**第三天**：灵隐寺与西溪湿地游览 \n\n- 早上：来到灵隐寺，体验浓厚的禅意文化，观看大量的佛教文化艺术品。\n- 中午：在灵隐寺附近的素斋馆体验一下素食文化。\n- 下午：前往杭州西溪国家湿地公园，参与自然保护活动，享受自然之美。\n- 晚上：返回酒店休息，结束美好的杭州之旅。\n\n以上就是为你定制的杭州三日旅行行程，希望你能在杭州度过愉快的时光！") 
    print(a) 
