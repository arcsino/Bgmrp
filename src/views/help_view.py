from pathlib import Path

import flet as ft

from views.components import BorderImage, ExplainContainer, SmallExplainContainer


class HelpView(ft.Column):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.visible = False
        self.scroll = ft.ScrollMode.AUTO
        self.controls = [
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            ExplainContainer(
                title="リソースパックの作成方法",
                body="以下にリソースパックの作成方法，作成時の注意点などを説明します．",
            ),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            # No.1
            SmallExplainContainer(
                title="1. アイコンを用意する",
                body="\n".join(
                    [
                        "リソースパックのアイコンにする画像を用意します．",
                        "画像ファイルはPNG形式で，縦横比が1:1になるようにしてください．",
                        "（例：512x512px，1024x1024px，etc.）",
                    ]
                ),
            ),
            BorderImage(src=Path("help1.png")),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            # No.2
            SmallExplainContainer(
                title="2. BGMを用意する",
                body="\n".join(
                    [
                        "追加するBGM，オーディオを用意します．",
                        "オーディオファイルはOGG形式で，アーティスト情報などの不要な情報は追加しないでください．",
                        "※ウェブサイトのOGGコンバーターを使う場合は，ウイルスが入ったファイルをダウンロードしないよう，信頼の出来るものを利用してください．",
                    ]
                ),
            ),
            BorderImage(src=Path("help2.png")),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            # No.3
            SmallExplainContainer(
                title="3. プロジェクトを作成する",
                body="\n".join(
                    [
                        "プロジェクトとはリソースパック作成時の情報（名前，説明，アイコン，etc.）を保存するための物です．",
                        "一度作成したリソースパックに追加でBGMを設定したい時に，また0から設定し直す必要がなくなります．",
                        "※C:\\Users\\[ユーザー名]\\.bgmrpにあるフォルダを削除すると，保存していたプロジェクトの情報は全て失われます．",
                        "※保存していたアイコンの画像ファイルとBGMのオーディオファイルを移動したり削除すると，プロジェクトの情報は失われます．",
                    ]
                ),
            ),
            BorderImage(src=Path("help3.png")),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            # No.4
            SmallExplainContainer(
                title="4. プロジェクトを編集する",
                body="編集ボタンを押すと，作成するリソースパックを編集することが出来ます．",
            ),
            BorderImage(src=Path("help4.png")),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            # No.5
            SmallExplainContainer(
                title="5. リソースパックの名前を入力する",
                body="\n".join(
                    [
                        "空欄だと作成できません．",
                        "また，安全のため半角英数字にすることをお勧めします．",
                    ]
                ),
            ),
            BorderImage(src=Path("help5.png")),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            # No.6
            SmallExplainContainer(
                title="6. リソースパックの説明を入力する",
                body="\n".join(
                    [
                        "空欄だと作成できません．",
                        "また，安全のため半角英数字にすることをお勧めします．",
                    ]
                ),
            ),
            BorderImage(src=Path("help6.png")),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            # No.7
            SmallExplainContainer(
                title="7. リソースパックのアイコンを選択する",
                body="用意しておいたアイコンの画像を選択してください．",
            ),
            BorderImage(src=Path("help7.png")),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            # No.8
            SmallExplainContainer(
                title="8. BGMを選択する",
                body="\n".join(
                    [
                        "用意しておいたオーディオを選択してください．",
                        "※複数選択した場合，BGMはランダムに再生されます．（マイクラの仕様）",
                    ]
                ),
            ),
            BorderImage(src=Path("help8.png")),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            # No.9
            SmallExplainContainer(
                title="9. BGMの音量を設定する",
                body="\n".join(
                    [
                        "100%で変更なしです．",
                        "普通に聴いて音量が大きい場合は，音量を下げてください．",
                        "※あまり大きすぎると効果音がかき消されます．",
                    ]
                ),
            ),
            BorderImage(src=Path("help9.png")),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            # No.10
            SmallExplainContainer(
                title="10. バージョンを設定する",
                body="\n".join(
                    [
                        "プレイするマイクラのバージョンに合わせてください．",
                        "違うバージョンで使おうとすると，警告が出る場合があります．",
                    ]
                ),
            ),
            BorderImage(src=Path("help10.png")),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            # No.11
            SmallExplainContainer(
                title="11. 保存する",
                body="プロジェクトの保存は，右上のアイコンを押すとできます．",
            ),
            BorderImage(src=Path("help11.png")),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            # No.12
            SmallExplainContainer(
                title="12. 作成する",
                body="\n".join(
                    [
                        "「作成する」のボタンを押すと，設定内容に不備がなければ保存先を選択するダイアログが出てきます．",
                        "無事作成されると以下の画像のようになります．",
                    ]
                ),
            ),
            BorderImage(src=Path("help12.png")),
            ft.Divider(color=ft.Colors.TRANSPARENT),  # margin
            # No.13
            SmallExplainContainer(
                title="13. エラーについて",
                body="\n".join(
                    [
                        "設定内容に不備があれば発生します．",
                        "不備がないのに発生したり，見知らないエラーが出た場合は，私に知らせてください．"
                        "fletの仕様でドキュメントフォルダにfletフォルダができることがありますが，これは削除しても問題ありません．",
                    ]
                ),
            ),
            BorderImage(src=Path("help13.png")),
        ]
