# 動画から顔を検出するプログラム
mp4ファイルを指定すると、その動画を10秒おきに抽出し、その中から指定された顔を検出します。

## 必要なインストール

### Pythonパッケージ

以下のコマンドを実行して、必要なPythonパッケージをインストールしてください：

```bash
pip install opencv-python
```

```bash
pip install dlib
```

```bash
pip install face_recognition
```


また、以下のツールもインストールが必要です：

1. CMake
   - ダウンロード先: https://cmake.org/download/
   - インストール手順:
     1. 上記リンクから、お使いのOSに適したバージョンをダウンロードします。
     2. ダウンロードしたインストーラーを実行し、画面の指示に従ってインストールします。

2. C++コンパイラ（Visual Studio Build Tools）
   - ダウンロード先: https://visualstudio.microsoft.com/ja/visual-cpp-build-tools/
   - インストール手順:
     1. 上記リンクから、Visual Studio Build Toolsをダウンロードします。
     2. インストーラーを実行し、「C++によるデスクトップ開発」を選択します。
     3. 「インストール」をクリックし、インストールを完了させます。

注意: これらのツールのインストールには管理者権限が必要な場合があります。