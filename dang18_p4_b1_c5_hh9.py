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


def bt_dang18_p4_b1_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.randint(4, 15)

        tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (-1.5,0);
\\coordinate (B) at (1.5,0);
\\coordinate (C) at (120:1.5);
\\coordinate (D) at (-120:1.5);
\\coordinate (H) at (-0.75,0);
\\coordinate (E) at ($(A)!2!(C)$);
\\coordinate (F) at ($(B)!2!(D)$);
\\draw[line width=1pt] (O) circle (1.5);
\\draw[line width=1pt] (A)--(B);
\\draw[line width=1pt] (C)--(D);
\\draw[line width=1pt] (E)--(C) (F)--(D);
\\draw[line width=1pt, dashed] (E)--(F) (B)--(C) (A)--(D);
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (B) circle (1pt) node[right] {$B$};
\\fill (C) circle (1pt) node[above] {$C$};
\\fill (D) circle (1pt) node[below] {$D$};
\\fill (H) circle (1pt) node[below left] {$H$};
\\fill (E) circle (1pt) node[below left] {$E$};
\\fill (F) circle (1pt) node[above right] {$F$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho đường tròn $(O; %s\\text{ cm})$ đường kính $AB$ và điểm $C$ nằm trên đường tròn $(O)$ ($C \\ne A, C \\ne B$). Vẽ dây cung $CD$ vuông góc với $AB$ tại $H$. Gọi $E$ là điểm đối xứng với $C$ qua điểm $A$, và $F$ là điểm đối xứng với $D$ qua điểm $B$ (như hình vẽ). \\\\
a) Chứng minh rằng hai đường thẳng $CE$ và $DF$ vuông góc với nhau. \\\\
b) Gọi $I$ là trung điểm của đoạn thẳng $EF$. Chứng minh rằng điểm $I$ đối xứng với điểm $H$ qua tâm $O$.
%s''' % (R, tikz_code))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì đường kính $AB$ đi qua tâm $O$ và vuông góc với dây cung $CD$ tại $H$ nên $AB$ là trục đối xứng của đường tròn $(O)$, suy ra $C$ và $D$ đối xứng với nhau qua $AB$.\\\\
Do đó $AB$ là đường trung trực của $CD$, nên $BC = BD$, suy ra $\\widehat{CBA} = \\widehat{DBA}$.\\\\
Tam giác $ACB$ có đường trung tuyến $CO = R = \\dfrac{AB}{2}$ nên tam giác $ACB$ vuông tại $C$, do đó $\\widehat{CAB} + \\widehat{CBA} = 90^{\\circ}$.\\\\
Thay $\\widehat{CBA} = \\widehat{DBA}$, ta được $\\widehat{CAB} + \\widehat{DBA} = 90^{\\circ}$.\\\\
Vì $E$ đối xứng với $C$ qua $A$ và $F$ đối xứng với $D$ qua $B$ nên đường thẳng $CE$ trùng với đường thẳng $AC$ và đường thẳng $DF$ trùng với đường thẳng $BD$.\\\\
Từ $\\widehat{CAB} + \\widehat{DBA} = 90^{\\circ}$ suy ra đường thẳng $AC$ vuông góc với đường thẳng $BD$, tức là $CE \\perp DF$.
\\item Vì $C$ và $D$ đối xứng với nhau qua đường thẳng $AB$ nên $H$ là trung điểm của đoạn thẳng $CD$.\\\\
Gọi $M$ là trung điểm của $CF$. Trong tam giác $CEF$, $AM$ là đường trung bình (do $A$ là trung điểm $CE$, $M$ là trung điểm $CF$).\\\\
Xét hai tam giác $OAE$ và $OBF$ hoặc dùng tính chất đường trung bình: gọi $K$ là giao điểm thứ hai của $DO$ với $(O)$ thì $K$ đối xứng với $D$ qua $O$, nên $AKBD$ là hình chữ nhật, suy ra $AK // BD$ và $AK = BD$.\\\\
Lại có $BF = BD$ và $B$ nằm giữa $D, F$ nên $AK // BF$ và $AK = BF$, do đó $AKFB$ là hình bình hành, suy ra $KF // AB$ và $KF = AB$.\\\\
Mặt khác, $K$ đối xứng với $D$ qua $O$ và $D$ đối xứng với $C$ qua $AB$ nên $CK // AB$ và $CK = 2OH$ (trong $\\Delta KCD$ có $O$ là trung điểm $KD$, $H$ là trung điểm $CD$ nên $OH$ là đường trung bình, suy ra $KC // AB$ và $KC = 2OH$).\\\\
Do $A$ là trung điểm $EC$ và $O$ là trung điểm $AB$, xét hình thang $ECKF$ (có $EC$ và $KF$ cắt nhau, $KC // AB // KF$): $C, K, F$ thẳng hàng với $CF = CK + KF = 2OH + AB$.\\\\
Trong tam giác $CEF$ có $A$ là trung điểm $CE$ và $I$ là trung điểm $EF$ nên $AI // CF$ và $AI = \\dfrac{CF}{2} = OH + \\dfrac{AB}{2} = OH + OA$.\\\\
Do $AI // AB$ và điểm $I$ nằm cùng phía với $B$ so với $A$ nên $I$ nằm trên đường thẳng $AB$ và $OI = AI - OA = OH$. Vì $H$ và $I$ nằm về hai phía của $O$ nên $O$ là trung điểm của $HI$, tức là $I$ đối xứng với $H$ qua tâm $O$.
\\end{enumEX}''')

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
