class wL:
    """wL / File class"""
    
    def __init__(self):
        """wL / New object."""
        self.dict : dict = {}
        
    def pack(self, open = 'todo', master : str = '', tab : str = '    ', depth : int = 0) -> str:
        """wL / Pack a wL object and return it as a txt str."""
        txt : str = ''
        if open == 'todo'           : dic = self.dict
        else                        : dic = open
        if isinstance(dic, list) or isinstance(dic, dict) :
            if depth > 0                 : txt += tab * (depth -1) + '<' + master + '>' + '\n'
            if   isinstance(dic, list)   : # notice than a wL should not contain lists, but dicts with str numbers as keys.
                for i in range(len(dic)) : txt += self.pack(open = dic[i], master = str(i), tab = tab, depth = depth + 1)
            elif isinstance(dic, dict)   :
                for key in dic.keys()    : txt += self.pack(open = dic[key], master = str(key), tab = tab, depth = depth + 1)
            if depth > 0                 : txt += tab * (depth -1) + '<!>' + '\n'
        elif isinstance(dic, str)   : txt += tab * (depth -1) + '<' + master + '=' + str(dic) + '>' + '\n'
        return txt
                    
    def unpack(self, file : str) -> dict:
        """wl / Open wL file in self. Overwritte former dict. Also return wL dict."""
        path = []
        newD = {}
        wRNm = False
        for letter in file:
            if   letter == ' ': '' #blank space
            elif letter == '<':
                wRNm = True
                name = ''
                data = None
            elif letter == '>':
                # sauvegarder la donnée
                if data is None :
                    if len(name) == 0 : name = 'null'
                    if name[0] != '!' :
                        path.append(name)
                        newD = self.__save(newD, path, value = {})
                    else             : path.pop()
                else            : newD = self.__save(newD, path + [name], data)
            elif letter == '=':
                wRNm = False
                data = ''
            else              :
                if wRNm == True : name += letter
                else            : data += letter
        self.dict = newD
        return newD
                
    def __save(self, dic : dict, path : list, value = 'null') -> dict:
        """wL / Functions / In a dict 'dic', following a list 'path of keys', edit last key with value, and return dic."""
        copyDic = dic # copy of dic
        # Iterate all except last key
        for key in path[:-1]:
            if key not in copyDic : copyDic[key] = {}  # Create a new dict if path is not valid
            copyDic = copyDic[key]
        # Edit last key
        copyDic[path[-1]] = value
        return dic
        
    def exportXML(self, open = 'todo', master = 'xml', tab : str = '    ', depth : int = 0) -> str:
        """wL / Pack a wL object as an XML file and return it as a txt str."""
        txt : str = ''
        if open == 'todo'           : dic = self.dict
        else                        : dic = open
        if isinstance(dic, list) or isinstance(dic, dict) :
            if depth >= 0                 : txt += tab * depth + '<' + master + '>' + '\n'
            if   isinstance(dic, list)   : 
                for i in range(len(dic)) : txt += self.exportXML(open = dic[i], master = str(i), tab = tab, depth = depth + 1)
            elif isinstance(dic, dict)   :
                for key in dic.keys()    : txt += self.exportXML(open = dic[key], master = str(key), tab = tab, depth = depth + 1)
            if depth >= 0                 : txt += tab * depth + '</' + master + '>' + '\n'
        elif isinstance(dic, str)   :
            txt += tab * depth + '<' + master + '>' + str(dic) + '</' + master + '>' + '\n'
        return txt
    
    def get(self) -> dict:
        """wL / Get wL dict."""
        return self.dict 
    
def wL_info() -> str:
    """wL / Print informations about wL. Return current version id."""
    print('\n\n ##### wL ############### \n')
    print('  - by wilhelm43     [ https://scratch.mit.edu/users/wilhelm43/ ]')
    print('  - version          [ 00103 ]')
    print('  - licence CC-BY-SA [ https://creativecommons.org/licenses/by-sa/4.0/ ]')
    print('\n wL is a "markup" "metalanguage" designed to store arbitrary data in a format that is both human-readable and machine-readable.')
    print(' The design goals of wL emphasize elementary simplicity, generality, stability, and usability across all Programming language.')
    print(' Plus, wL format does not contain no data specialisation or typing, for a linear read.')
    print('\n ######################## \n\n')
    return '00103'
