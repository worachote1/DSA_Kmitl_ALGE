n = "怪当華盛失略冗乏巨凹岩島天花魚力耳正幸歴本侍盗勉病店用宝市令事隣丁零夕璽召断女仲妹恋卒入停聴打焼糸居宅氷傘紅"
data = {"อาหาร": ["穀糧米飯食飲喫摂煮蒸焼炊漬塩糖味辛甘酸渋渇飢餓飽茶菓汁醸酵酢酒酌酔",[]],
        "เครื่องนุ่มห่ม": ["絹綿麻紡績錘繰繊維糸布革織染絞裁縫編繕衣服装紋襟帯緒結縛着被履脱裸帽冠靴",[]],
        "ที่อยู่อาศัย": ["住居活宿泊寝睡眠休憩暇掃飾粧畳床柱戸扉棚欄桟壁窓廊階壇台井溝室斎房寮庭園",[]]}

for item in n: 
    
    for ss_type in list(data.keys()):
        if(item in data[ss_type][0]):
            data[ss_type][1].append(item)

for key,value in data.items():
    print(key+" : "+" ".join(value[1]))


