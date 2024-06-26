import streamlit as st
import json
import os
import random

# チームごとのクイズデータ（例）
quiz_data = {
    #ここからJ1
    "コンサドーレ札幌": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2015", "2016", "2017", "2018"], "answer": "2016"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ドーレくん", "レディくん", "リボンちゃん", "フレップ"], "answer": "ドーレくん"},
        {"question": "監督の名前は何ですか？", "options": ["ミハイロ・ペトロヴィッチ", "ペトロヴィッチ", "ミハイロ", "ペトロ"], "answer": "ミハイロ・ペトロヴィッチ"},
        {"question": "本拠地はどこですか？", "options": ["札幌ドーム", "味の素スタジアム", "埼玉スタジアム", "日産スタジアム"], "answer": "札幌ドーム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["1996", "1997", "1998", "1999"], "answer": "1997"}
    ],
    "浦和レッズ": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2006", "2007", "2008", "2009"], "answer": "2007"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["レディア", "フレディア", "フレンディア", "ブレディア"], "answer": "レディア"},
        {"question": "監督の名前は何ですか？", "options": ["リカルド・ロドリゲス", "ロドリゲス", "リカルド", "ロドリ"], "answer": "リカルド・ロドリゲス"},
        {"question": "本拠地はどこですか？", "options": ["埼玉スタジアム", "味の素スタジアム", "日産スタジアム", "札幌ドーム"], "answer": "埼玉スタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["1992", "1994", "1995", "1996"], "answer": "1992"}
    ],
    "ＦＣ東京": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2009", "2010", "2011", "2012"], "answer": "2012"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ドロンパ", "ドロン", "ドンパ", "ドロンペ"], "answer": "ドロンパ"},
        {"question": "監督の名前は何ですか？", "options": ["長谷川健太", "健太", "長谷川", "ケンタ"], "answer": "長谷川健太"},
        {"question": "本拠地はどこですか？", "options": ["味の素スタジアム", "日産スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "味の素スタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["1999", "2000", "2001", "2002"], "answer": "1999"}
    ],
    "ＦＣ町田ゼルビア": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2019", "2020", "2021", "2022"], "answer": "2021"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ゼルビー", "ゼルビ", "ゼル", "ビー"], "answer": "ゼルビー"},
        {"question": "監督の名前は何ですか？", "options": ["ランコ・ポポヴィッチ", "ポポヴィッチ", "ランコ", "ポポ"], "answer": "ランコ・ポポヴィッチ"},
        {"question": "本拠地はどこですか？", "options": ["町田市立陸上競技場", "味の素スタジアム", "日産スタジアム", "埼玉スタジアム"], "answer": "町田市立陸上競技場"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2000", "2001", "2002", "2003"], "answer": "2001"}
    ],
    "横浜Ｆ・マリノス": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2017", "2018", "2019", "2020"], "answer": "2019"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["マリノスケ", "マリノス", "マリモ", "マリノ"], "answer": "マリノスケ"},
        {"question": "監督の名前は何ですか？", "options": ["アンジェ・ポステコグルー", "ポステコグルー", "アンジェ", "ポステ"], "answer": "アンジェ・ポステコグルー"},
        {"question": "本拠地はどこですか？", "options": ["日産スタジアム", "等々力陸上競技場", "味の素スタジアム", "埼玉スタジアム"], "answer": "日産スタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["1992", "1993", "1994", "1995"], "answer": "1993"}
    ],
    "アルビレックス新潟": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2014", "2015", "2016", "2017"], "answer": "2015"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["アルビ", "レックス", "スワン", "ニータン"], "answer": "アルビ"},
        {"question": "監督の名前は何ですか？", "options": ["アルビレックス", "レックス", "アルビ", "スワン"], "answer": "アルビレックス"},
        {"question": "本拠地はどこですか？", "options": ["デンカビッグスワンスタジアム", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "デンカビッグスワンスタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["1996", "1997", "1998", "1999"], "answer": "1999"}
    ],
    "名古屋グランパス": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2010", "2011", "2012", "2013"], "answer": "2011"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["グランパスくん", "グラン", "パス", "くん"], "answer": "グランパスくん"},
        {"question": "監督の名前は何ですか？", "options": ["マッシモ・フィッカデンティ", "フィッカデンティ", "マッシモ", "フィカ"], "answer": "マッシモ・フィッカデンティ"},
        {"question": "本拠地はどこですか？", "options": ["豊田スタジアム", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "豊田スタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["1992", "1993", "1994", "1995"], "answer": "1993"}
    ],
    "ガンバ大阪": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2014", "2015", "2016", "2017"], "answer": "2015"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ガンバボーイ", "ガンバ", "ボーイ", "ガンバ君"], "answer": "ガンバボーイ"},
        {"question": "監督の名前は何ですか？", "options": ["宮本恒靖", "恒靖", "宮本", "ツネ"], "answer": "宮本恒靖"},
        {"question": "本拠地はどこですか？", "options": ["パナソニックスタジアム吹田", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "パナソニックスタジアム吹田"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["1992", "1993", "1994", "1995"], "answer": "1993"}
    ],
    "ヴィッセル神戸": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2019", "2020", "2021", "2022"], "answer": "2020"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["モーヴィ", "ヴィッセル", "モー", "ヴィ"], "answer": "モーヴィ"},
        {"question": "監督の名前は何ですか？", "options": ["トルステン・フィンク", "フィンク", "トルステン", "トル"], "answer": "トルステン・フィンク"},
        {"question": "本拠地はどこですか？", "options": ["ノエビアスタジアム神戸", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "ノエビアスタジアム神戸"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["1995", "1996", "1997", "1998"], "answer": "1996"}
    ],
    "アビスパ福岡": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2018", "2019", "2020", "2021"], "answer": "2020"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["アビスパくん", "アビ", "スパ", "アビ君"], "answer": "アビスパくん"},
        {"question": "監督の名前は何ですか？", "options": ["長谷部茂利", "茂利", "長谷部", "シゲ"], "answer": "長谷部茂利"},
        {"question": "本拠地はどこですか？", "options": ["ベスト電器スタジアム", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "ベスト電器スタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["1996", "1997", "1998", "1999"], "answer": "1997"}
    ],
    "鹿島アントラーズ": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2015", "2016", "2017", "2018"], "answer": "2016"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["しかお", "しか", "お", "アントラー"], "answer": "しかお"},
        {"question": "監督の名前は何ですか？", "options": ["大岩剛", "剛", "大岩", "ツヨシ"], "answer": "大岩剛"},
        {"question": "本拠地はどこですか？", "options": ["カシマサッカースタジアム", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "カシマサッカースタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["1991", "1992", "1993", "1994"], "answer": "1992"}
    ],
    "柏レイソル": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2011", "2012", "2013", "2014"], "answer": "2012"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["レイくん", "レイ", "くん", "レイちゃん"], "answer": "レイくん"},
        {"question": "監督の名前は何ですか？", "options": ["ネルシーニョ", "シーニョ", "ネル", "ネルシ"], "answer": "ネルシーニョ"},
        {"question": "本拠地はどこですか？", "options": ["三協フロンテア柏スタジアム", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "三協フロンテア柏スタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["1993", "1994", "1995", "1996"], "answer": "1994"}
    ],
    "東京ヴェルディ": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2005", "2006", "2007", "2008"], "answer": "2007"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ヴェルディくん", "ヴェル", "ディ", "くん"], "answer": "ヴェルディくん"},
        {"question": "監督の名前は何ですか？", "options": ["永井秀樹", "秀樹", "永井", "ヒデキ"], "answer": "永井秀樹"},
        {"question": "本拠地はどこですか？", "options": ["味の素スタジアム", "日産スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "味の素スタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2001", "2002", "2003", "2004"], "answer": "2002"}
    ],
    "川崎フロンターレ": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2017", "2018", "2019", "2020"], "answer": "2020"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ふろん太", "ふろん助", "ふろん次郎", "ふろん三郎"], "answer": "ふろん太"},
        {"question": "監督の名前は何ですか？", "options": ["鬼木達", "鬼木剛", "鬼木誠", "鬼木勇"], "answer": "鬼木達"},
        {"question": "本拠地はどこですか？", "options": ["等々力陸上競技場", "日産スタジアム", "味の素スタジアム", "埼玉スタジアム"], "answer": "等々力陸上競技場"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["1995", "1996", "1997", "1998"], "answer": "1997"}
    ],
    "湘南ベルマーレ": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2014", "2015", "2016", "2017"], "answer": "2015"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["キングベル", "ベル", "キング", "ベル君"], "answer": "キングベル"},
        {"question": "監督の名前は何ですか？", "options": ["チョウ・キジェ", "キジェ", "チョウ", "チョ"], "answer": "チョウ・キジェ"},
        {"question": "本拠地はどこですか？", "options": ["ＢＭＷスタジアム", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "ＢＭＷスタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["1999", "2000", "2001", "2002"], "answer": "1999"}
    ],
    "ジュビロ磐田": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2002", "2003", "2004", "2005"], "answer": "2002"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ジュビロくん", "ジュビ", "ロ", "ジュビ君"], "answer": "ジュビロくん"},
        {"question": "監督の名前は何ですか？", "options": ["名波浩", "浩", "名波", "ナナミ"], "answer": "名波浩"},
        {"question": "本拠地はどこですか？", "options": ["ヤマハスタジアム", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "ヤマハスタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["1994", "1995", "1996", "1997"], "answer": "1994"}
    ],
    "京都サンガＦ.Ｃ.": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2014", "2015", "2016", "2017"], "answer": "2015"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["サンガくん", "サン", "ガ", "サン君"], "answer": "サンガくん"},
        {"question": "監督の名前は何ですか？", "options": ["加藤望", "望", "加藤", "カトウ"], "answer": "加藤望"},
        {"question": "本拠地はどこですか？", "options": ["京都市西京極総合運動公園陸上競技場", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "京都市西京極総合運動公園陸上競技場"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["1993", "1994", "1995", "1996"], "answer": "1994"}
    ],
    "セレッソ大阪": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2010", "2011", "2012", "2013"], "answer": "2011"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ロビー", "ロビ", "ビー", "ロビ君"], "answer": "ロビー"},
        {"question": "監督の名前は何ですか？", "options": ["レヴィー・クルピ", "クルピ", "レヴィー", "レヴィ"], "answer": "レヴィー・クルピ"},
        {"question": "本拠地はどこですか？", "options": ["ヤンマースタジアム長居", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "ヤンマースタジアム長居"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["1994", "1995", "1996", "1997"], "answer": "1994"}
    ],
    "サンフレッチェ広島": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2012", "2013", "2014", "2015"], "answer": "2013"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["サンチェ", "サン", "チェ", "サン君"], "answer": "サンチェ"},
        {"question": "監督の名前は何ですか？", "options": ["森保一", "一", "森保", "モリ"], "answer": "森保一"},
        {"question": "本拠地はどこですか？", "options": ["エディオンスタジアム広島", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "エディオンスタジアム広島"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["1992", "1993", "1994", "1995"], "answer": "1992"}
    ],
    "サガン鳥栖": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2014", "2015", "2016", "2017"], "answer": "2015"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ウィントス", "ウィン", "トス", "ウィン君"], "answer": "ウィントス"},
        {"question": "監督の名前は何ですか？", "options": ["金明輝", "明輝", "金", "メイ"], "answer": "金明輝"},
        {"question": "本拠地はどこですか？", "options": ["駅前不動産スタジアム", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "駅前不動産スタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["1997", "1998", "1999", "2000"], "answer": "1999"}
    ],
    #J1ここまで
    #ここからJ2
        "ベガルタ仙台": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2009", "2010", "2011", "2012"], "answer": "2010"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ベガッ太", "ベガ", "太", "ベガ太"], "answer": "ベガッ太"},
        {"question": "監督の名前は何ですか？", "options": ["渡邉晋", "晋", "渡邉", "ワタナベ"], "answer": "渡邉晋"},
        {"question": "本拠地はどこですか？", "options": ["ユアテックスタジアム仙台", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "ユアテックスタジアム仙台"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["1999", "2000", "2001", "2002"], "answer": "1999"}
    ],
    "モンテディオ山形": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2014", "2015", "2016", "2017"], "answer": "2015"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ディーオ", "ディ", "オ", "ディオ君"], "answer": "ディーオ"},
        {"question": "監督の名前は何ですか？", "options": ["木山隆之", "隆之", "木山", "キヤマ"], "answer": "木山隆之"},
        {"question": "本拠地はどこですか？", "options": ["ＮＤソフトスタジアム山形", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "ＮＤソフトスタジアム山形"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["1996", "1997", "1998", "1999"], "answer": "1999"}
    ],
    "水戸ホーリーホック": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2008", "2009", "2010", "2011"], "answer": "2009"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ホーリーくん", "ホーリー", "くん", "ホーリーちゃん"], "answer": "ホーリーくん"},
        {"question": "監督の名前は何ですか？", "options": ["秋葉忠宏", "忠宏", "秋葉", "アキバ"], "answer": "秋葉忠宏"},
        {"question": "本拠地はどこですか？", "options": ["ケーズデンキスタジアム水戸", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "ケーズデンキスタジアム水戸"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2000", "2001", "2002", "2003"], "answer": "2000"}
    ],
    "ザスパクサツ群馬": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2013", "2014", "2015", "2016"], "answer": "2014"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ヤス", "スパ", "クサツ", "ザス"], "answer": "ヤス"},
        {"question": "監督の名前は何ですか？", "options": ["秋田豊", "豊", "秋田", "アキタ"], "answer": "秋田豊"},
        {"question": "本拠地はどこですか？", "options": ["正田醤油スタジアム群馬", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "正田醤油スタジアム群馬"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2002", "2003", "2004", "2005"], "answer": "2005"}
    ],
    "横浜ＦＣ": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2018", "2019", "2020", "2021"], "answer": "2020"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["フリ丸", "フリ", "丸", "フリ君"], "answer": "フリ丸"},
        {"question": "監督の名前は何ですか？", "options": ["下平隆宏", "隆宏", "下平", "シモヒラ"], "answer": "下平隆宏"},
        {"question": "本拠地はどこですか？", "options": ["ニッパツ三ツ沢球技場", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "ニッパツ三ツ沢球技場"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["1999", "2000", "2001", "2002"], "answer": "1999"}
    ],
    "清水エスパルス": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["1999", "2000", "2001", "2002"], "answer": "2001"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["パルちゃん", "パル", "ちゃん", "パル君"], "answer": "パルちゃん"},
        {"question": "監督の名前は何ですか？", "options": ["平岡宏章", "宏章", "平岡", "ヒラオカ"], "answer": "平岡宏章"},
        {"question": "本拠地はどこですか？", "options": ["ＩＡＩスタジアム日本平", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "ＩＡＩスタジアム日本平"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["1992", "1993", "1994", "1995"], "answer": "1992"}
    ],
    "ファジアーノ岡山": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2015", "2016", "2017", "2018"], "answer": "2016"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ファジ丸", "ファジ", "丸", "ファジ君"], "answer": "ファジ丸"},
        {"question": "監督の名前は何ですか？", "options": ["有馬賢二", "賢二", "有馬", "アリマ"], "answer": "有馬賢二"},
        {"question": "本拠地はどこですか？", "options": ["シティライトスタジアム", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "シティライトスタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2009", "2010", "2011", "2012"], "answer": "2009"}
    ],
    "徳島ヴォルティス": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2013", "2014", "2015", "2016"], "answer": "2014"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ヴォルタ", "ヴォル", "タ", "ヴォル君"], "answer": "ヴォルタ"},
        {"question": "監督の名前は何ですか？", "options": ["ポヤトス", "ポ", "ヤトス", "トス"], "answer": "ポヤトス"},
        {"question": "本拠地はどこですか？", "options": ["鳴門・大塚スポーツパークポカリスエットスタジアム", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "鳴門・大塚スポーツパークポカリスエットスタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2005", "2006", "2007", "2008"], "answer": "2005"}
    ],
    "Ｖ・ファーレン長崎": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2017", "2018", "2019", "2020"], "answer": "2018"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ヴィヴィくん", "ヴィヴィ", "くん", "ヴィヴィ君"], "answer": "ヴィヴィくん"},
        {"question": "監督の名前は何ですか？", "options": ["手倉森誠", "誠", "手倉森", "テグ"], "answer": "手倉森誠"},
        {"question": "本拠地はどこですか？", "options": ["トランスコスモススタジアム長崎", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "トランスコスモススタジアム長崎"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2005", "2006", "2007", "2008"], "answer": "2005"}
    ],
    "大分トリニータ": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2008", "2009", "2010", "2011"], "answer": "2008"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ニータン", "ニー", "タン", "ニータン君"], "answer": "ニータン"},
        {"question": "監督の名前は何ですか？", "options": ["片野坂知宏", "知宏", "片野坂", "カタノサカ"], "answer": "片野坂知宏"},
        {"question": "本拠地はどこですか？", "options": ["昭和電工ドーム大分", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "昭和電工ドーム大分"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["1999", "2000", "2001", "2002"], "answer": "1999"}
    ],
    "ブラウブリッツ秋田": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2020", "2021", "2022", "2023"], "answer": "2021"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ブラウ", "ブリッツ", "秋田", "ブラウ君"], "answer": "ブラウ"},
        {"question": "監督の名前は何ですか？", "options": ["吉田達磨", "達磨", "吉田", "ヨシダ"], "answer": "吉田達磨"},
        {"question": "本拠地はどこですか？", "options": ["ソユースタジアム", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "ソユースタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2014", "2015", "2016", "2017"], "answer": "2014"}
    ],
    "いわきＦＣ": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2017", "2018", "2019", "2020"], "answer": "2018"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["いわ", "いわき", "いわき君", "いわちゃん"], "answer": "いわき"},
        {"question": "監督の名前は何ですか？", "options": ["安田佑太", "佑太", "安田", "ヤスダ"], "answer": "安田佑太"},
        {"question": "本拠地はどこですか？", "options": ["いわきグリーンフィールド", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "いわきグリーンフィールド"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2015", "2016", "2017", "2018"], "answer": "2015"}
    ],
    "栃木ＳＣ": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2014", "2015", "2016", "2017"], "answer": "2015"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["トッキー", "トキ", "トッキ", "トッキー君"], "answer": "トッキー"},
        {"question": "監督の名前は何ですか？", "options": ["田坂和昭", "和昭", "田坂", "タサカ"], "answer": "田坂和昭"},
        {"question": "本拠地はどこですか？", "options": ["栃木県グリーンスタジアム", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "栃木県グリーンスタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2009", "2010", "2011", "2012"], "answer": "2009"}
    ],
    "ジェフユナイテッド千葉": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2005", "2006", "2007", "2008"], "answer": "2006"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ジェフィ", "ジェフ", "フィ", "ジェフィ君"], "answer": "ジェフィ"},
        {"question": "監督の名前は何ですか？", "options": ["江尻篤彦", "篤彦", "江尻", "エジリ"], "answer": "江尻篤彦"},
        {"question": "本拠地はどこですか？", "options": ["フクダ電子アリーナ", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "フクダ電子アリーナ"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2005", "2006", "2007", "2008"], "answer": "2005"}
    ],
    "ヴァンフォーレ甲府": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2012", "2013", "2014", "2015"], "answer": "2013"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ヴァン君", "ヴァン", "君", "ヴァンちゃん"], "answer": "ヴァン君"},
        {"question": "監督の名前は何ですか？", "options": ["吉田達磨", "達磨", "吉田", "ヨシダ"], "answer": "吉田達磨"},
        {"question": "本拠地はどこですか？", "options": ["山梨中銀スタジアム", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "山梨中銀スタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["1999", "2000", "2001", "2002"], "answer": "1999"}
    ],
    "藤枝ＭＹＦＣ": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2015", "2016", "2017", "2018"], "answer": "2016"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["フジッピー", "フジ", "ッピー", "フジ君"], "answer": "フジッピー"},
        {"question": "監督の名前は何ですか？", "options": ["志村謄", "謄", "志村", "シムラ"], "answer": "志村謄"},
        {"question": "本拠地はどこですか？", "options": ["藤枝総合運動公園", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "藤枝総合運動公園"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2009", "2010", "2011", "2012"], "answer": "2009"}
    ],
    "レノファ山口ＦＣ": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2018", "2019", "2020", "2021"], "answer": "2020"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["レノ", "ファ", "レノ君", "ファ君"], "answer": "レノ"},
        {"question": "監督の名前は何ですか？", "options": ["霜田正浩", "正浩", "霜田", "シモダ"], "answer": "霜田正浩"},
        {"question": "本拠地はどこですか？", "options": ["維新みらいふスタジアム", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "維新みらいふスタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2015", "2016", "2017", "2018"], "answer": "2015"}
    ],
    "愛媛ＦＣ": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2013", "2014", "2015", "2016"], "answer": "2015"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["オレンジくん", "オレンジ", "くん", "オレンジ君"], "answer": "オレンジくん"},
        {"question": "監督の名前は何ですか？", "options": ["川井健太", "健太", "川井", "カワイ"], "answer": "川井健太"},
        {"question": "本拠地はどこですか？", "options": ["ニンジニアスタジアム", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "ニンジニアスタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2006", "2007", "2008", "2009"], "answer": "2006"}
    ],
    "ロアッソ熊本": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2018", "2019", "2020", "2021"], "answer": "2020"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ロアッソ君", "ロア", "君", "ロア君"], "answer": "ロアッソ君"},
        {"question": "監督の名前は何ですか？", "options": ["大木武", "武", "大木", "オオキ"], "answer": "大木武"},
        {"question": "本拠地はどこですか？", "options": ["えがお健康スタジアム", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "えがお健康スタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2008", "2009", "2010", "2011"], "answer": "2008"}
    ],
    "鹿児島ユナイテッドＦＣ": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2016", "2017", "2018", "2019"], "answer": "2017"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ガンバ", "バンザイ", "イケ", "ユニくん"], "answer": "ユニくん"},
        {"question": "監督の名前は何ですか？", "options": ["金鍾成", "鍾成", "金", "ジョン"], "answer": "金鍾成"},
        {"question": "本拠地はどこですか？", "options": ["白波スタジアム", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "白波スタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2015", "2016", "2017", "2018"], "answer": "2015"}
    ],
    #J2ここまで
    #ここからJ3
        "ヴァンラーレ八戸": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2017", "2018", "2019", "2020"], "answer": "2019"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ヴァン太", "ヴァン次郎", "ヴァン助", "ヴァン君"], "answer": "ヴァン太"},
        {"question": "監督の名前は何ですか？", "options": ["秋田豊", "豊", "秋田", "アキタ"], "answer": "秋田豊"},
        {"question": "本拠地はどこですか？", "options": ["ダイハツスタジアム", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "ダイハツスタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2014", "2015", "2016", "2017"], "answer": "2014"}
    ],
    "福島ユナイテッドＦＣ": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2015", "2016", "2017", "2018"], "answer": "2016"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["福島くん", "福島", "くん", "福島君"], "answer": "福島くん"},
        {"question": "監督の名前は何ですか？", "options": ["田坂和昭", "和昭", "田坂", "タサカ"], "answer": "田坂和昭"},
        {"question": "本拠地はどこですか？", "options": ["とうほう・みんなのスタジアム", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "とうほう・みんなのスタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2014", "2015", "2016", "2017"], "answer": "2014"}
    ],
    "Ｙ．Ｓ．Ｃ．Ｃ．横浜": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2015", "2016", "2017", "2018"], "answer": "2016"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ヨコくん", "ヨコ", "くん", "ヨコ君"], "answer": "ヨコくん"},
        {"question": "監督の名前は何ですか？", "options": ["樋口靖洋", "靖洋", "樋口", "ヒグチ"], "answer": "樋口靖洋"},
        {"question": "本拠地はどこですか？", "options": ["ニッパツ三ツ沢球技場", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "ニッパツ三ツ沢球技場"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2012", "2013", "2014", "2015"], "answer": "2012"}
    ],
    "松本山雅ＦＣ": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2014", "2015", "2016", "2017"], "answer": "2015"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ガンズくん", "ガンズ", "くん", "ガンズ君"], "answer": "ガンズくん"},
        {"question": "監督の名前は何ですか？", "options": ["反町康治", "康治", "反町", "ソリマチ"], "answer": "反町康治"},
        {"question": "本拠地はどこですか？", "options": ["サンプロアルウィン", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "サンプロアルウィン"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2009", "2010", "2011", "2012"], "answer": "2009"}
    ],
    "カターレ富山": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2011", "2012", "2013", "2014"], "answer": "2012"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ライカくん", "ライカ", "くん", "ライカ君"], "answer": "ライカくん"},
        {"question": "監督の名前は何ですか？", "options": ["石崎信弘", "信弘", "石崎", "イシザキ"], "answer": "石崎信弘"},
        {"question": "本拠地はどこですか？", "options": ["富山県総合運動公園陸上競技場", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "富山県総合運動公園陸上競技場"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2008", "2009", "2010", "2011"], "answer": "2008"}
    ],
    "アスルクラロ沼津": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2017", "2018", "2019", "2020"], "answer": "2018"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["アスル", "クラロ", "アスル君", "クラロ君"], "answer": "アスル"},
        {"question": "監督の名前は何ですか？", "options": ["高原直泰", "直泰", "高原", "タカハラ"], "answer": "高原直泰"},
        {"question": "本拠地はどこですか？", "options": ["愛鷹広域公園多目的競技場", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "愛鷹広域公園多目的競技場"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2006", "2007", "2008", "2009"], "answer": "2006"}
    ],
    "ＦＣ大阪": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2017", "2018", "2019", "2020"], "answer": "2018"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["オー君", "オー", "君", "オーちゃん"], "answer": "オー君"},
        {"question": "監督の名前は何ですか？", "options": ["北村知隆", "知隆", "北村", "キタムラ"], "answer": "北村知隆"},
        {"question": "本拠地はどこですか？", "options": ["ヤンマースタジアム長居", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "ヤンマースタジアム長居"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2012", "2013", "2014", "2015"], "answer": "2012"}
    ],
    "ガイナーレ鳥取": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2014", "2015", "2016", "2017"], "answer": "2015"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ガイナ", "ナーレ", "ガイナ君", "ナーレ君"], "answer": "ガイナ"},
        {"question": "監督の名前は何ですか？", "options": ["布啓一郎", "啓一郎", "布", "ヌノ"], "answer": "布啓一郎"},
        {"question": "本拠地はどこですか？", "options": ["とりぎんバードスタジアム", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "とりぎんバードスタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2007", "2008", "2009", "2010"], "answer": "2007"}
    ],
    "ＦＣ今治": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2016", "2017", "2018", "2019"], "answer": "2017"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["バリィさん", "バリィ", "さん", "バリィ君"], "answer": "バリィさん"},
        {"question": "監督の名前は何ですか？", "options": ["小松原学", "学", "小松原", "コマツバラ"], "answer": "小松原学"},
        {"question": "本拠地はどこですか？", "options": ["ありがとうサービス. 夢スタジアム", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "ありがとうサービス. 夢スタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2014", "2015", "2016", "2017"], "answer": "2014"}
    ],
    "テゲバジャーロ宮崎": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2018", "2019", "2020", "2021"], "answer": "2020"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["テゲバ", "ジャーロ", "テゲバ君", "ジャーロ君"], "answer": "テゲバ"},
        {"question": "監督の名前は何ですか？", "options": ["三浦泰年", "泰年", "三浦", "ミウラ"], "answer": "三浦泰年"},
        {"question": "本拠地はどこですか？", "options": ["ユニリーバスタジアム新富", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "ユニリーバスタジアム新富"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2015", "2016", "2017", "2018"], "answer": "2015"}
    ],
    "いわてグルージャ盛岡": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2016", "2017", "2018", "2019"], "answer": "2017"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["いわてくん", "いわて", "くん", "いわて君"], "answer": "いわてくん"},
        {"question": "監督の名前は何ですか？", "options": ["小野寺秀", "秀", "小野寺", "オノデラ"], "answer": "小野寺秀"},
        {"question": "本拠地はどこですか？", "options": ["いわてスタジアム", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "いわてスタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2015", "2016", "2017", "2018"], "answer": "2015"}
    ],
    "大宮アルディージャ": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2004", "2005", "2006", "2007"], "answer": "2005"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["アルディ", "ディ", "アル", "アルディ君"], "answer": "アルディ"},
        {"question": "監督の名前は何ですか？", "options": ["伊藤彰", "彰", "伊藤", "イトウ"], "answer": "伊藤彰"},
        {"question": "本拠地はどこですか？", "options": ["ＮＡＣＫ５スタジアム大宮", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "ＮＡＣＫ５スタジアム大宮"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["1999", "2000", "2001", "2002"], "answer": "1999"}
    ],
    "ＳＣ相模原": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2014", "2015", "2016", "2017"], "answer": "2015"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ギオンくん", "ギオン", "くん", "ギオン君"], "answer": "ギオンくん"},
        {"question": "監督の名前は何ですか？", "options": ["三浦泰年", "泰年", "三浦", "ミウラ"], "answer": "三浦泰年"},
        {"question": "本拠地はどこですか？", "options": ["相模原ギオンスタジアム", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "相模原ギオンスタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2008", "2009", "2010", "2011"], "answer": "2008"}
    ],
    "ＡＣ長野パルセイロ": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2013", "2014", "2015", "2016"], "answer": "2014"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["パル君", "パル", "君", "パルちゃん"], "answer": "パル君"},
        {"question": "監督の名前は何ですか？", "options": ["相馬直樹", "直樹", "相馬", "ソウマ"], "answer": "相馬直樹"},
        {"question": "本拠地はどこですか？", "options": ["長野Uスタジアム", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "長野Uスタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2007", "2008", "2009", "2010"], "answer": "2007"}
    ],
    "エーゲン金沢": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2014", "2015", "2016", "2017"], "answer": "2015"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["エー君", "エー", "君", "エーちゃん"], "answer": "エー君"},
        {"question": "監督の名前は何ですか？", "options": ["安達亮", "亮", "安達", "アダチ"], "answer": "安達亮"},
        {"question": "本拠地はどこですか？", "options": ["西部緑地公園陸上競技場", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "西部緑地公園陸上競技場"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2005", "2006", "2007", "2008"], "answer": "2005"}
    ],
    "ＦＣ岐阜": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2012", "2013", "2014", "2015"], "answer": "2013"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ギッフィー", "ギフ", "フィー", "ギフ君"], "answer": "ギッフィー"},
        {"question": "監督の名前は何ですか？", "options": ["北野誠", "誠", "北野", "キタノ"], "answer": "北野誠"},
        {"question": "本拠地はどこですか？", "options": ["長良川競技場", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "長良川競技場"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2001", "2002", "2003", "2004"], "answer": "2001"}
    ],
    "奈良クラブ": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2017", "2018", "2019", "2020"], "answer": "2018"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ナッシー", "ナラ", "クラブ", "ナラ君"], "answer": "ナッシー"},
        {"question": "監督の名前は何ですか？", "options": ["石井正忠", "正忠", "石井", "イシイ"], "answer": "石井正忠"},
        {"question": "本拠地はどこですか？", "options": ["ならでんフィールド", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "ならでんフィールド"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2013", "2014", "2015", "2016"], "answer": "2013"}
    ],
    "カマタマーレ讃岐": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2014", "2015", "2016", "2017"], "answer": "2015"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["さぬぴー", "さぬ", "ぴー", "さぬ君"], "answer": "さぬぴー"},
        {"question": "監督の名前は何ですか？", "options": ["田坂和昭", "和昭", "田坂", "タサカ"], "answer": "田坂和昭"},
        {"question": "本拠地はどこですか？", "options": ["ピカラスタジアム", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "ピカラスタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2010", "2011", "2012", "2013"], "answer": "2010"}
    ],
    "ギラヴァンツ北九州": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2019", "2020", "2021", "2022"], "answer": "2020"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["ギラン", "ヴァン", "ギラ君", "ヴァン君"], "answer": "ギラン"},
        {"question": "監督の名前は何ですか？", "options": ["小林伸二", "伸二", "小林", "コバヤシ"], "answer": "小林伸二"},
        {"question": "本拠地はどこですか？", "options": ["ミクニワールドスタジアム北九州", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "ミクニワールドスタジアム北九州"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2010", "2011", "2012", "2013"], "answer": "2010"}
    ],
    "ＦＣ琉球": [
        {"question": "最後に優勝した年は何年ですか？", "options": ["2018", "2019", "2020", "2021"], "answer": "2019"},
        {"question": "マスコットキャラクターの名前は何ですか？", "options": ["りゅうくん", "りゅう", "くん", "りゅう君"], "answer": "りゅうくん"},
        {"question": "監督の名前は何ですか？", "options": ["樋口靖洋", "靖洋", "樋口", "ヒグチ"], "answer": "樋口靖洋"},
        {"question": "本拠地はどこですか？", "options": ["タピック県総ひやごんスタジアム", "味の素スタジアム", "埼玉スタジアム", "札幌ドーム"], "answer": "タピック県総ひやごんスタジアム"},
        {"question": "今のチーム名で活動が開始されたのは何年ですか？", "options": ["2013", "2014", "2015", "2016"], "answer": "2013"}
    ],
}


# 表示する問題数
NUM_QUESTIONS = 3

# ユーザー情報の入力
st.title("Jリーグクイズアプリ")
st.write("このクイズは各チーム全５問のうち、３問をランダムに出題し、点数を付けています。")

# チーム選択
team = st.selectbox("チームを選択してください", list(quiz_data.keys()))

# クイズの表示と採点処理
if st.button("クイズを開始"):
    # クイズの質問を選択し、ランダムに3問抽出
    questions = random.sample(quiz_data[team], NUM_QUESTIONS)
    
    # ユーザーの回答を保存するためのセッションステート
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = [None] * len(questions)
    if 'quiz_started' not in st.session_state:
        st.session_state.quiz_started = True
        st.session_state.questions = questions
        st.session_state.show_answers = False

if 'quiz_started' in st.session_state and st.session_state.quiz_started:
    # クイズの質問を表示
    questions = st.session_state.questions
    for idx, q in enumerate(questions):
        st.write(f"Q{idx+1}: {q['question']}")
        current_selection = st.session_state.user_answers[idx]
        if current_selection is not None:
            st.session_state.user_answers[idx] = st.radio("", q["options"], index=q["options"].index(current_selection), key=f"q{idx}")
        else:
            st.session_state.user_answers[idx] = st.radio("", q["options"], key=f"q{idx}")

    if st.button("採点"):
        score = sum(1 for idx, q in enumerate(questions) if st.session_state.user_answers[idx] == q["answer"])
        
        # 結果を大きなフォントで表示
        st.markdown(f"<h1>あなたの得点は: {score}/{len(questions)}</h1>", unsafe_allow_html=True)
        st.session_state.show_answers = True

if 'show_answers' in st.session_state and st.session_state.show_answers:
    # 各質問の答えを表示
    questions = st.session_state.questions
    for idx, q in enumerate(questions):
        st.write(f"Q{idx+1}: {q['question']}")
        user_answer = st.session_state.user_answers[idx]
        st.write(f"あなたの回答: {user_answer}")
        st.write(f"正解: {q['answer']}")
        if user_answer == q['answer']:
            st.markdown("<span style='color: blue; font-size: large;'>正解！</span>", unsafe_allow_html=True)
        else:
            st.markdown("<span style='color: red; font-size: large;'>不正解！</span>", unsafe_allow_html=True)
        st.write("---")
