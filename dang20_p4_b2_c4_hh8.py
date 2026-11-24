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

def bt_dang20_p4_b2_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ac = random.choice([24, 28, 32, 36, 40])
        bd = random.choice([18, 20, 24, 28, 30])
        mn = ac // 2
        mq = bd // 2
        cv = (mn + mq) * 2
        dt = mn * mq

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.5,3.2);
\\coordinate (B) at (0,1.2);
\\coordinate (C) at (2.2,0);
\\coordinate (D) at (4.5,1.8);
\\coordinate (M) at ($(A)!0.5!(B)$);
\\coordinate (N) at ($(B)!0.5!(C)$);
\\coordinate (P) at ($(C)!0.5!(D)$);
\\coordinate (Q) at ($(D)!0.5!(A)$);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (M)--(N)--(P)--(Q)--cycle;
\\draw[line width=1pt, dashed] (A)--(C) (B)--(D);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (C) circle (1pt) node[below] {$C$};
\\fill (D) circle (1pt) node[right] {$D$};
\\fill (M) circle (1pt) node[above left] {$M$};
\\fill (N) circle (1pt) node[below left] {$N$};
\\fill (P) circle (1pt) node[below right] {$P$};
\\fill (Q) circle (1pt) node[above right] {$Q$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Bác Nam sở hữu một mảnh vườn hình tứ giác $ABCD$ có hai con mương tưới tiêu thẳng góc với nhau chạy dọc theo hai đường chéo $AC = %s\\text{ m}$ và $BD = %s\\text{ m}$. Bác muốn quy hoạch khu vực trồng rau sạch ở phần lõi hình tứ giác $MNPQ$ được giới hạn bởi các đoạn thẳng nối trung điểm bốn bờ rào $AB, BC, CD, DA$ (như hình vẽ).\\
a) Chứng minh khu vực trồng rau sạch $MNPQ$ có dạng hình chữ nhật.\\
b) Tính chu vi hàng rào bao quanh khu vực trồng rau sạch $MNPQ$ và diện tích phần đất trồng rau sạch đó.%s''' % (fmt_num(ac), fmt_num(bd), hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Xét tam giác $ABC$ và tam giác $ADC$, ta có $MN$ và $PQ$ lần lượt là các đường trung bình nên $MN // AC$, $PQ // AC$ và $MN = PQ = \\dfrac{1}{2}AC$.\\
Suy ra $MN // PQ$ và $MN = PQ$, do đó tứ giác $MNPQ$ là hình bình hành.\\
Xét tam giác $ABD$ có $MQ$ là đường trung bình nên $MQ // BD$.\\
Vì $MN // AC$, $MQ // BD$ và hai con mương $AC \\perp BD$ nên $MN \\perp MQ$, hay $\\widehat{QMN} = 90^\\circ$.\\
Hình bình hành $MNPQ$ có một góc vuông nên khu vực trồng rau sạch $MNPQ$ có dạng hình chữ nhật.
\\item Chiều dài và chiều rộng của khu vực hình chữ nhật $MNPQ$ là:\\
$MN = \\dfrac{1}{2}AC = \\dfrac{1}{2} \\cdot %s = %s\\text{ m}$;\\
$MQ = \\dfrac{1}{2}BD = \\dfrac{1}{2} \\cdot %s = %s\\text{ m}$.\\
Chu vi hàng rào bao quanh khu vực trồng rau sạch $MNPQ$ là:\\
$2(MN + MQ) = 2(%s + %s) = %s\\text{ m}$.\\
Diện tích phần đất trồng rau sạch $MNPQ$ là:\\
$S_{MNPQ} = MN \\cdot MQ = %s \\cdot %s = %s\\text{ m}^2$.
\\end{enumEX}''' % (fmt_num(ac), fmt_num(mn), fmt_num(bd), fmt_num(mq), fmt_num(mn), fmt_num(mq), fmt_num(cv), fmt_num(mn), fmt_num(mq), fmt_num(dt)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
