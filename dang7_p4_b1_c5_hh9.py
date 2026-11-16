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


def bt_dang7_p4_b1_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.randint(4, 15)

        tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (40:1.8);
\\coordinate (B) at (-40:1.8);
\\coordinate (C) at (220:1.8);
\\coordinate (D) at (140:1.8);
\\draw[line width=1pt] (O) circle (1.8);
\\draw[line width=1pt] (-2.3,0)--(2.3,0) node[above] {$d$};
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
\\draw[line width=1pt, dashed] (A)--(C) (B)--(D);
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (A) circle (1pt) node[above right] {$A$};
\\fill (B) circle (1pt) node[below right] {$B$};
\\fill (C) circle (1pt) node[below left] {$C$};
\\fill (D) circle (1pt) node[above left] {$D$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho đường tròn $(O; %s\\text{ cm})$, đường thẳng $d$ đi qua $O$ và điểm $A \\in (O)$ nhưng $A \\notin d$. Gọi $B$ là điểm đối xứng với $A$ qua $d$; gọi $C$ và $D$ lần lượt là điểm đối xứng với $A$ và $B$ qua $O$ (như hình vẽ). \\\\
a) Chứng minh rằng tứ giác $ABCD$ là hình chữ nhật. \\\\
b) Chứng minh rằng hai điểm $C$ và $D$ đối xứng với nhau qua đường thẳng $d$.
%s''' % (R, tikz_code))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì đường thẳng $d$ đi qua tâm $O$ nên $d$ là trục đối xứng của $(O)$, suy ra điểm $B$ đối xứng với $A$ qua $d$ cũng thuộc đường tròn $(O)$.\\\\
Tương tự, $O$ là tâm đối xứng của $(O)$ nên hai điểm $C, D$ đối xứng với $A, B$ qua $O$ cũng thuộc đường tròn $(O)$.\\\\
Do $C$ và $D$ lần lượt đối xứng với $A$ và $B$ qua tâm $O$ nên $O$ là trung điểm của cả hai đoạn thẳng $AC$ và $BD$.\\\\
Suy ra tứ giác $ABCD$ có hai đường chéo $AC$ và $BD$ cắt nhau tại trung điểm $O$ của mỗi đường nên $ABCD$ là hình bình hành.\\\\
Mặt khác, bốn điểm $A, B, C, D$ cùng thuộc đường tròn $(O; %s\\text{ cm})$ nên $AC = BD = 2R = %s\\text{ cm}$. Hình bình hành có hai đường chéo bằng nhau nên tứ giác $ABCD$ là hình chữ nhật.
\\item Vì $ABCD$ là hình chữ nhật nên $CD // AB$ và $CD = AB$.\\\\
Vì $B$ đối xứng với $A$ qua đường thẳng $d$ nên $d$ là đường trung trực của $AB$, suy ra $d \\perp AB$.\\\\
Do $CD // AB$ và $d \\perp AB$ nên $d \\perp CD$. Lại có $d$ đi qua tâm $O$ và $OC = OD = R$ nên $O$ nằm trên đường trung trực của $CD$.\\\\
Đường thẳng $d$ đi qua $O$ và vuông góc với $CD$ nên $d$ là đường trung trực của đoạn thẳng $CD$. Vậy hai điểm $C$ và $D$ đối xứng với nhau qua đường thẳng $d$.
\\end{enumEX}''' % (R, 2 * R))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
