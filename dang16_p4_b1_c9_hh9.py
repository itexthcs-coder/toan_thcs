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


def bt_dang16_p4_b1_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.choice([12, 15, 18, 20, 24])

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (O) at (0,0);\n'
            '\\coordinate (A) at (240:2);\n'
            '\\coordinate (B) at (300:2);\n'
            '\\coordinate (C) at (110:2);\n'
            '\\coordinate (D) at (0.3,0.6);\n'
            '\\coordinate (K) at (78:2);\n'
            '\\draw[line width=1pt] (O) circle (2cm);\n'
            '\\draw[line width=1pt] (A)--(B) (A)--(C)--(B) (A)--(D)--(B);\n'
            '\\draw[line width=1pt, dashed] (O)--(A) (O)--(B) (D)--(K)--(B);\n'
            '\\fill (O) circle (1pt) node[left] {$O$};\n'
            '\\fill (A) circle (1pt) node[below left] {$A$};\n'
            '\\fill (B) circle (1pt) node[below right] {$B$};\n'
            '\\fill (C) circle (1pt) node[above left] {$C$};\n'
            '\\fill (D) circle (1pt) node[below] {$D$};\n'
            '\\fill (K) circle (1pt) node[above] {$K$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Trong một nhà hát có mặt bằng hình tròn tâm $O$, bán kính $R = %s\\text{ m}$, sân khấu được bố trí dọc theo dây cung $AB$ có độ dài $AB = %s\\text{ m}$. Khán giả ngồi ở khu vực cung lớn $AB$ để theo dõi vở diễn như hình vẽ.\\'
            'a) Tính góc nhìn $\\widehat{ACB}$ từ một ghế ngồi $C$ sát tường bao trên cung lớn $AB$ tới hai mép sân khấu $A$ và $B$.\\'
            'b) Một khán giả khác ngồi tại vị trí $D$ ở bên trong hội trường (nằm trong miền giới hạn bởi dây $AB$ và cung lớn $AB$). Hãy so sánh góc nhìn $\\widehat{ADB}$ của khán giả này với góc nhìn $\\widehat{ACB}$ ở câu a) và giải thích bằng kiến thức hình học.\\'
            'c) Nếu ban tổ chức mở rộng chiều ngang sân khấu thành dây cung $A\'B\'$ đi qua tâm $O$ (đường kính của nhà hát) thì góc nhìn từ mọi ghế ngồi trên nửa đường tròn đối diện tới hai mép sân khấu mới bằng bao nhiêu độ?\n%s'
            % (R, R, hinh_ve)
        )

        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Xét $\\triangle OAB$ có $OA = OB = AB = %s\\text{ m}$ nên $\\triangle OAB$ là tam giác đều, suy ra góc ở tâm $\\widehat{AOB} = 60^\\circ$.\\'
            'Trong đường tròn $(O)$, góc nội tiếp $\\widehat{ACB}$ và góc ở tâm $\\widehat{AOB}$ cùng chắn cung nhỏ $AB$ nên $\\widehat{ACB} = \\dfrac{1}{2}\\widehat{AOB} = \\dfrac{60^\\circ}{2} = 30^\\circ$.\n'
            '\\item Kéo dài $AD$ cắt cung lớn $AB$ tại điểm $K$. Vì hai góc nội tiếp $\\widehat{AKB}$ và $\\widehat{ACB}$ cùng chắn cung nhỏ $AB$ nên $\\widehat{AKB} = \\widehat{ACB} = 30^\\circ$.\\'
            'Xét $\\triangle DKB$, góc $\\widehat{ADB}$ là góc ngoài tại đỉnh $D$ nên $\\widehat{ADB} = \\widehat{AKB} + \\widehat{KBD} > \\widehat{AKB} = 30^\\circ$. Vậy góc nhìn $\\widehat{ADB}$ lớn hơn góc nhìn $\\widehat{ACB}$.\n'
            '\\item Khi sân khấu mới $A\'B\'$ là đường kính của đường tròn $(O)$, mọi góc nhìn từ các ghế ngồi trên nửa đường tròn đối diện đều là góc nội tiếp chắn nửa đường tròn nên đều có số đo bằng $90^\\circ$.\n'
            '\\end{enumEX}'
            % (R)
        )

    # Xuất câu hỏi với lời giải
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
