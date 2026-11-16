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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang15_p4_b1_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_htc = [(6, 8, 7, 3, 4, 3, 4, 5), (12, 16, 14, 6, 8, 6, 8, 10), (10, 24, 17, 5, 12, 5, 12, 13)]
        ab, cd, h, ha, kd, ok, oh, R = random.choice(bo_htc)

        tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (D) at (-1.6,0);
\\coordinate (C) at (1.6,0);
\\coordinate (A) at (-1.2,2.1);
\\coordinate (B) at (1.2,2.1);
\\coordinate (H) at (0,2.1);
\\coordinate (K) at (0,0);
\\coordinate (O) at (0,0.9);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
\\draw[line width=1pt] (H)--(K);
\\draw[line width=1pt, dashed] (O)--(A) (O)--(D);
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below left] {$D$};
\\fill (H) circle (1pt) node[above] {$H$};
\\fill (K) circle (1pt) node[below] {$K$};
\\fill (O) circle (1pt) node[right] {$O$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho hình thang cân $ABCD$ ($AB // CD$, $AB < CD$) có hai đáy $AB = %s\\text{ cm}$, $CD = %s\\text{ cm}$ và đường cao bằng $%s\\text{ cm}$ (như hình vẽ). \\\\
a) Chứng minh rằng tồn tại một đường tròn đi qua cả bốn đỉnh $A, B, C, D$ và tâm $O$ của đường tròn đó nằm trên trục đối xứng của hình thang cân $ABCD$. \\\\
b) Xác định vị trí chính xác của tâm $O$ và tính bán kính của đường tròn đi qua bốn đỉnh $A, B, C, D$.
%s''' % (ab, cd, h, tikz_code))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Gọi $H, K$ lần lượt là trung điểm của hai đáy $AB, CD$. Theo tính chất hình thang cân, đường thẳng $HK$ là đường trung trực chung của $AB$ và $CD$, nên $HK$ là trục đối xứng của hình thang cân $ABCD$.\\\\
Gọi $O$ là giao điểm của đường trung trực cạnh bên $AD$ với đường thẳng $HK$.\\\\
Vì $O$ nằm trên đường trung trực của $AD$, $AB$, $CD$ nên $OA = OD$, $OA = OB$ và $OD = OC$.\\\\
Suy ra $OA = OB = OC = OD$, do đó bốn đỉnh $A, B, C, D$ cùng thuộc đường tròn tâm $O$ nằm trên trục đối xứng $HK$.
\\item Ta có $HA = \\dfrac{AB}{2} = %s\\text{ cm}$, $KD = \\dfrac{CD}{2} = %s\\text{ cm}$ và đường cao $HK = %s\\text{ cm}$.\\\\
Đặt $OK = x$ ($0 < x < %s$), suy ra $OH = %s - x$. Áp dụng định lí Pythagore cho hai tam giác vuông $OHA$ và $OKD$, từ $OA^2 = OD^2$ ta có:\\\\
$(%s - x)^2 + %s^2 = x^2 + %s^2 \\Leftrightarrow %s - %s x + %s = %s \\Leftrightarrow %s x = %s \\Leftrightarrow x = %s\\text{ cm}$.\\\\
Vậy tâm $O$ nằm trên đoạn thẳng $HK$, cách đáy lớn $CD$ một khoảng $OK = %s\\text{ cm}$ (và cách đáy nhỏ $AB$ một khoảng $OH = %s\\text{ cm}$).\\\\
Bán kính của đường tròn đi qua bốn đỉnh $A, B, C, D$ là:\\\\
$R = OD = \\sqrt{OK^2 + KD^2} = \\sqrt{%s^2 + %s^2} = %s\\text{ cm}$.
\\end{enumEX}''' % (ha, kd, h, h, h, h, ha, kd, h**2, 2*h, ha**2, kd**2, 2*h, h**2 + ha**2 - kd**2, ok, ok, oh, ok, kd, R))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
