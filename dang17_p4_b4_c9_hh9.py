# -*- coding: utf-8 -*-
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


def bt_dang17_p4_b4_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ten_hs = random.choice(["Hà", "Lan", "Hoa", "An"])

        hinh_tikz = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (126:0.75);
\\coordinate (B) at (54:0.75);
\\coordinate (C) at (-18:0.75);
\\coordinate (D) at (-90:0.75);
\\coordinate (E) at (198:0.75);
\\coordinate (P1) at (90:1.95);
\\coordinate (P2) at (18:1.95);
\\coordinate (P3) at (-54:1.95);
\\coordinate (P4) at (-126:1.95);
\\coordinate (P5) at (162:1.95);
\\draw[line width=1pt] (P1)--(B)--(P2)--(C)--(P3)--(D)--(P4)--(E)--(P5)--(A)--cycle;
\\draw[line width=1pt, dashed] (A)--(B)--(C)--(D)--(E)--cycle;
\\draw[line width=1pt, dashed] (P1)--(D);
\\fill (P1) circle (1pt) node[above] {$P$};
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below] {$D$};
\\fill (E) circle (1pt) node[below left] {$E$};
\\end{tikzpicture}
\\end{center}'''

        noidungcauhoi = ('''Bạn %s muốn cắt một hình ngôi sao năm cánh đều có phần lõi bên trong là một ngũ giác đều $ABCDE$ (như hình vẽ). Để cắt nhanh và cân đối, bạn %s gấp đôi tờ giấy theo trục đối xứng đi qua một đỉnh cánh sao $P$, vẽ một nửa hình ngôi sao rồi dùng kéo cắt thẳng theo nét vẽ. Hãy tính số đo góc nhọn tạo bởi lưỡi kéo và nếp gấp đôi tờ giấy lúc đầu, giải thích rõ các bước suy luận hình học. %s'''
                         % (ten_hs, ten_hs, hinh_tikz))

        loigiai = ('''Ngũ giác đều $ABCDE$ có $5$ cạnh bằng nhau nội tiếp một đường tròn nên góc ở tâm chắn mỗi cạnh bằng $\\frac{360^\\circ}{5} = 72^\\circ$. \\\\
Suy ra số đo mỗi góc trong của ngũ giác đều $ABCDE$ bằng $180^\\circ - 72^\\circ = 108^\\circ$. \\\\
Xét tam giác cánh sao $PAB$ cân tại $P$ (do tính đối xứng của ngôi sao năm cánh đều). Hai góc ở đáy $\\widehat{PAB}$ và $\\widehat{PBA}$ lần lượt kề bù với hai góc trong $\\widehat{EAB} = 108^\\circ$ và $\\widehat{CBA} = 108^\\circ$ của ngũ giác đều $ABCDE$, nên:
$$\\widehat{PAB} = \\widehat{PBA} = 180^\\circ - 108^\\circ = 72^\\circ.$$
Trong tam giác $PAB$, tổng ba góc bằng $180^\\circ$ nên số đo góc nhọn ở đỉnh cánh sao $P$ là:
$$\\widehat{APB} = 180^\\circ - (\\widehat{PAB} + \\widehat{PBA}) = 180^\\circ - 2 \\cdot 72^\\circ = 36^\\circ.$$
Vì nếp gấp đôi tờ giấy là trục đối xứng của ngôi sao đi qua đỉnh $P$ nên nếp gấp là tia phân giác của góc $\\widehat{APB}$. \\\\
Vậy góc nhọn tạo bởi lưỡi kéo (cắt theo cạnh $PA$ hoặc $PB$) và nếp gấp đôi tờ giấy lúc đầu bằng:
$$\\frac{\\widehat{APB}}{2} = \\frac{36^\\circ}{2} = 18^\\circ.$$''')

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
