def setw(string,length:int,location='left', spacing=0):
    stuffing = '.'
    string = str(string)
    len_string = len(string)
    if len_string >= length:
        length = len_string
    if location == 'left':
        return spacing * stuffing + string + (length - len_string - spacing)*stuffing
    elif location == 'mid':
        out = round((length - len_string)/2) * stuffing + string + round((length - len_string)/2)*stuffing
        if len(out) > length:
            out = out[-length:]
        elif len(out) < length:
            out = out + (length - len(out)) * stuffing
        return spacing * stuffing + out

def setw_Q(string,length:int, location='left'):
    string = strB2Q(str(string))
    len_string = len(string)
    if len_string >= length:
        length = len_string
    if location == 'left':
        return string + (length - len_string)*'　'
    elif location == 'mid':
        out = round((length - len_string)/2)*'　' + string + round((length - len_string)/2)*'　'
        if len(out) > length:
            out = out[-length:]
        return out

def strB2Q(ustring):
    ss = []
    for s in ustring:
        rstring = ""
        for uchar in s:
            inside_code = ord(uchar)
            if inside_code == 32:  # 全形空格直接轉換
                inside_code = 12288
            elif (inside_code >= 33 and inside_code <= 126):  # 全形字元（除空格）根據關係轉化
                inside_code += 65248
            rstring += chr(inside_code)
        ss.append(rstring)
    return ''.join(ss)