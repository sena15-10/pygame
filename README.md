# 異変ゲーム
<dl>
　<dt>遊び方</dt>
<dd>このゲームは元のマップからの異変を探していくゲームです。それぞれのマップに一つだけの異変があります。異変があれば進んでもらって「ENTER」
という文字が画面上に出てきます。そこの場所でENTERキーを押し「Yes/no」の選択肢を選ばされます。

異変があればYes
異変がなければNo

という風にします。異変有　＝　異変有　異変無　＝　異変無　の二パターンのみカウントが進みます。
カウントは8まであります。　ちょうど8になるとゲームが終了します。
</dd>
間違っていてもカウントは減りません。

<dt>追記</dt>
<dd>異変がない場合は見たい場合はMap.pyの変数Random_index　=　０に上書きしてみてください
もし覚えた場合Random_indexは元の状態に戻してください(random_index = r.choice([0, r.randint(1, len(all_maps) - 1),r.randint(1, len(all_maps) - 1)]))
</dd>
</dl>
