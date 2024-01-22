from avgEmoValues import *

# See https://note.nkmk.me/python-pandas-option-display/
# pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 150)
pd.set_option('display.unicode.east_asian_width', True)

# valence: 感情価
# arousal: 覚醒度
# dominance: 支配性
# https://www.jstage.jst.go.jp/article/itej/67/12/67_J463/_pdf
LEXNAMES = ["valence", "arousal", "dominance"]
LEXPATH = "lexicons/NRC-VAD-Lexicon.csv"
LEXICON = read_lexicon(LEXPATH, LEXNAMES)

# --lexNames valence dominance
# --savePath sample_data/sample_outputs



text = """
Turkey is a captivating country that exudes charm and beauty at every turn. So, I'm happy!!!
"""
# text = """
# I love NY!
# """

for LEXNAME in LEXNAMES:
    df_lex = prep_dim_lexicon(LEXICON, LEXNAME)
    print(LEXNAME + " lexicon length: " + str(len(df_lex)))

    # CSV を読み込むバージョン
    # dataPath = "sample_data/sample_input.csv"
    # df = pd.read_csv(dataPath)
    # df_res = process_df(df, df_lex)
    # print(f"{df_res=}")

    numTokens, numLexTokens, avgLexVal = get_vals(text, df_lex)
    print(f"{numTokens=}, {numLexTokens=}, {avgLexVal=}")
