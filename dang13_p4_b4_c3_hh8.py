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


def bt_dang13_p4_b4_c3_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        canh_ab = random.choice([20, 30, 40, 50, 60])
        chu_vi = 2 * canh_ab

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (B) at (0,3);
\\coordinate (A) at (0,0);
\\coordinate (C) at (3,0);
\\coordinate (E) at (1.2,1.8);
\\coordinate (D) at (0,1.8);
\\coordinate (F) at (1.2,0);
\\draw[line width=1pt] (B)--(A)--(C)--cycle (E)--(D) (E)--(F) (D)--(F) (A)--(E);
\\draw[line width=1pt] (0,0.22)--(0.22,0.22)--(0.22,0);
\\draw[line width=1pt] (0,1.58)--(0.22,1.58)--(0.22,1.8);
\\draw[line width=1pt] (0.98,0)--(0.98,0.22)--(1.2,0.22);
\\fill (B) circle (1pt) node[above] {$B$};
\\fill (A) circle (1pt) node[below left] {$A$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (E) circle (1pt) node[above right] {$E$};
\\fill (D) circle (1pt) node[left] {$D$};
\\fill (F) circle (1pt) node[below] {$F$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Từ một tấm tôn hình tam giác vuông cân $ABC$ vuông tại $A$ có cạnh góc vuông $AB = AC = %s\\text{ cm}$, người thợ cắt ra một tấm tôn hình chữ nhật $ADEF$ sao cho $D \\in AB$, $E \\in BC$ và $F \\in AC$ ($E$ khác $B$ và $C$). \\\\
a) Chứng minh chu vi của tấm tôn hình chữ nhật $ADEF$ không phụ thuộc vào vị trí của điểm $E$ trên cạnh huyền $BC$ và tính giá trị chu vi đó. \\\\
b) Hỏi phải chọn điểm $E$ ở vị trí nào trên cạnh $BC$ để độ dài đường chéo $DF$ của tấm tôn hình chữ nhật là ngắn nhất? Vì sao? %s'''
                         % (canh_ab, hinh_ve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì $ADEF$ là hình chữ nhật nên $\\widehat{ADE} = 90^\\circ$, suy ra $\\triangle BDE$ vuông tại $D$. \\\\
Mặt khác, $\\triangle ABC$ vuông cân tại $A$ nên $\\widehat{DBE} = 45^\\circ$. \\\\
Tam giác $BDE$ vuông tại $D$ có $\\widehat{DBE} = 45^\\circ$ nên $\\triangle BDE$ vuông cân tại $D$, suy ra $DE = BD$. \\\\
Chu vi hình chữ nhật $ADEF$ bằng: \\\\
$2(AD + DE) = 2(AD + BD) = 2 \\cdot AB = 2 \\cdot %s = %s\\text{ cm}$ (không đổi với mọi vị trí của $E$ trên $BC$).
\\item Trong hình chữ nhật $ADEF$, hai đường chéo $DF$ và $AE$ bằng nhau nên $DF = AE$. \\\\
Do đó $DF$ ngắn nhất khi và chỉ khi $AE$ ngắn nhất. \\\\
Trong $\\triangle ABC$, đoạn thẳng $AE$ nối đỉnh $A$ với điểm $E$ trên cạnh $BC$ ngắn nhất khi $AE \\perp BC$ (quan hệ đường vuông góc và đường xiên). \\\\
Vì $\\triangle ABC$ vuông cân tại $A$ nên đường cao ứng với cạnh huyền $BC$ đồng thời là đường trung tuyến. \\\\
Vậy điểm $E$ phải là trung điểm của cạnh huyền $BC$.
\\end{enumEX}'''
                   % (canh_ab, chu_vi))
    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
