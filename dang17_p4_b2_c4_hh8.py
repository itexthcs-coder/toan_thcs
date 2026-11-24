import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def fmt_num(val):
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    return str(val).replace('.', ',')

def bt_dang17_p4_b2_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ab = random.choice([1.6, 1.8, 2.0, 2.2])
        bc = random.choice([1.2, 1.4, 1.5, 1.6])
        de = bc / 2

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (2.0,3.2);
\\coordinate (B) at (0,0);
\\coordinate (C) at (4.0,0);
\\coordinate (D) at ($(A)!0.5!(B)$);
\\coordinate (E) at ($(A)!0.5!(C)$);
\\coordinate (I) at ($(D)!0.5!(E)$);
\\coordinate (H) at ($(B)!0.5!(C)$);
\\draw[line width=1pt] (A)--(B) (A)--(C) (D)--(E);
\\draw[line width=1pt, dashed] (B)--(C) (A)--(H);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\fill (D) circle (1pt) node[left] {$D$};
\\fill (E) circle (1pt) node[right] {$E$};
\\fill (I) circle (1pt) node[above right] {$I$};
\\fill (H) circle (1pt) node[below] {$H$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Trong xây dựng dân dụng, người thợ sử dụng một chiếc thước chữ $A$ được cấu tạo từ hai thanh gỗ thẳng bằng nhau $AB = AC = %s\\text{ m}$ gắn bản lề tại đỉnh $A$, và một thanh ngang $DE$ bắt vít cố định vào trung điểm của $AB$ và $AC$ (như hình vẽ).\\
a) Khi mở thước sao cho khoảng cách giữa hai chân đế $B$ và $C$ trên mặt sàn là $%s\\text{ m}$, hãy tính chiều dài thanh ngang $DE$.\\
b) Từ đỉnh $A$, người thợ thả một dây dọi tự do. Chứng minh rằng nếu dây dọi đi qua đúng trung điểm $I$ của thanh ngang $DE$ thì mặt sàn $BC$ tại vị trí đặt thước hoàn toàn nằm ngang (vuông góc với phương thẳng đứng của dây dọi).%s''' % (fmt_num(ab), fmt_num(bc), hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Xét tam giác $ABC$ có $D, E$ lần lượt là trung điểm của $AB$ và $AC$ nên $DE$ là đường trung bình của tam giác $ABC$.\\
Theo tính chất đường trung bình của tam giác, chiều dài thanh ngang $DE$ là:\\
$DE = \\dfrac{1}{2}BC = \\dfrac{1}{2} \\cdot %s = %s\\text{ m}$.
\\item Vì $AB = AC$ nên tam giác $ABC$ cân tại $A$, lại có $AD = \\dfrac{1}{2}AB$ và $AE = \\dfrac{1}{2}AC$ nên $AD = AE$, suy ra tam giác $ADE$ cân tại $A$.\\
Vì dây dọi đi qua đỉnh $A$ và trung điểm $I$ của cạnh đáy $DE$ nên $AI$ là đường trung tuyến đồng thời là đường cao của tam giác cân $ADE$, suy ra $AI \\perp DE$.\\
Mặt khác, $DE$ là đường trung bình của tam giác $ABC$ nên $DE // BC$.\\
Từ $AI \\perp DE$ và $DE // BC$ suy ra $AI \\perp BC$. Vì dây dọi $AI$ có phương thẳng đứng nên đường thẳng $BC$ nằm ngang.
\\end{enumEX}''' % (fmt_num(bc), fmt_num(de)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
