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


def bt_dang20_p4_b1_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.randint(4, 15)

        tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (110:1.8);
\\coordinate (B) at (215:1.8);
\\coordinate (C) at (-35:1.8);
\\coordinate (D) at (-70:1.8);
\\coordinate (H) at (-0.616,0.289);
\\coordinate (M) at ($(B)!0.5!(C)$);
\\coordinate (H1) at (-0.616,-2.354);
\\draw[line width=1pt] (O) circle (1.8);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (B)--(H)--(C)--(D)--(B);
\\draw[line width=1pt, dashed] (A)--(D) (H)--(D) (H)--(H1);
\\fill (O) circle (1pt) node[above right] {$O$};
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\fill (D) circle (1pt) node[below right] {$D$};
\\fill (H) circle (1pt) node[above left] {$H$};
\\fill (M) circle (1pt) node[below right] {$M$};
\\fill (H1) circle (1pt) node[below] {$H'$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho tam giác $ABC$ nhọn ($AB < AC$) nội tiếp đường tròn $(O; %s\\text{ cm})$. Gọi $H$ là trực tâm của tam giác $ABC$ và $D$ là điểm đối xứng với $A$ qua tâm $O$ (như hình vẽ). \\\\
a) Chứng minh rằng tứ giác $BHCD$ là hình bình hành. \\\\
b) Gọi $M$ là trung điểm của cạnh $BC$ và $H'$ là điểm đối xứng với $H$ qua đường thẳng $BC$. Chứng minh rằng ba điểm $H, M, D$ thẳng hàng và điểm $H'$ nằm trên đường tròn $(O; %s\\text{ cm})$.
%s''' % (R, R, tikz_code))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì $D$ đối xứng với $A$ qua tâm $O$ nên $O$ là trung điểm của đoạn thẳng $AD$ và $AD = 2R$.\\\\
Xét tam giác $ABD$ có đường trung tuyến $BO = R = \\dfrac{AD}{2}$ nên tam giác $ABD$ vuông tại $B$, suy ra $BD \\perp AB$.\\\\
Mà $CH \\perp AB$ (do $H$ là trực tâm tam giác $ABC$) nên $BD // CH$.\\\\
Tương tự, tam giác $ACD$ vuông tại $C$ nên $CD \\perp AC$, mà $BH \\perp AC$ nên $CD // BH$.\\\\
Tứ giác $BHCD$ có các cặp cạnh đối song song ($BD // CH$ và $CD // BH$) nên $BHCD$ là hình bình hành.
\\item Vì $BHCD$ là hình bình hành nên hai đường chéo $BC$ và $HD$ cắt nhau tại trung điểm của mỗi đường.\\\\
Mà $M$ là trung điểm của $BC$ nên $M$ cũng là trung điểm của $HD$, suy ra ba điểm $H, M, D$ thẳng hàng.\\\\
Xét tam giác $H'HD$ có $M$ là trung điểm của $HD$ và $BC$ là đường trung trực của $HH'$ (do $H'$ đối xứng với $H$ qua $BC$).\\\\
Gọi $K$ là giao điểm của $BC$ và $HH'$ thì $K$ là trung điểm của $HH'$ và $BC \\perp HH'$ tại $K$. Trong tam giác $H'HD$, $MK$ là đường trung bình nên $MK // H'D$.\\\\
Do $K, M$ cùng thuộc đường thẳng $BC$ và $BC \\perp HH'$ nên $H'D \\perp HH'$, tức là $\\widehat{AH'D} = 90^{\\circ}$.\\\\
Xét tam giác $AH'D$ vuông tại $H'$ có $H'O$ là đường trung tuyến ứng với cạnh huyền $AD$, suy ra $OH' = \\dfrac{AD}{2} = R = %s\\text{ cm}$.\\\\
Vậy điểm $H'$ nằm trên đường tròn $(O; %s\\text{ cm})$.
\\end{enumEX}''' % (R, R))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
