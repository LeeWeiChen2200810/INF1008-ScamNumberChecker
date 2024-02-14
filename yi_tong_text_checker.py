import time

# Binary Search base code
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def count_hits_with_BS(arr1):
    start = time.perf_counter()
    special_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    special_chars_ascii_numbers = sorted([ord(char) for char in special_chars])
    hits = 0
    arr1_sorted = sorted(arr1)  # Create a sorted copy of the input array
    for num in special_chars_ascii_numbers:
        index = binary_search(arr1_sorted, num)
        while index != -1:
            hits += 1
            arr1_sorted.pop(index)  # Remove the found element to avoid counting duplicates
            index = binary_search(arr1_sorted, num)
    end = time.perf_counter()
    search = end - start
    return hits, search

# Red-Black Tree Node class definition
class RBNode:
    # Constructor to initialize a new node with the given keyword
    def __init__(self, keyword):
        self.keyword = keyword
        self.left = None
        self.right = None
        self.color = "red"  # All new nodes are initially colored red
        self.parent = None  # Parent attribute to track the parent node

# Perform a left rotation on the given pivot node in the Red-Black Tree.
def rotate_left(pivot):
    new_pivot = pivot.right
    pivot.right = new_pivot.left
    if new_pivot.left:
        new_pivot.left.parent = pivot
    new_pivot.left = pivot
    new_pivot.parent = pivot.parent
    pivot.parent = new_pivot
    return new_pivot

# Perform a right rotation on the given pivot node in the Red-Black Tree.
def rotate_right(pivot):
    new_pivot = pivot.left
    pivot.left = new_pivot.right
    if new_pivot.right:
        new_pivot.right.parent = pivot
    new_pivot.right = pivot
    new_pivot.parent = pivot.parent
    pivot.parent = new_pivot
    return new_pivot

#Fix the Red-Black Tree properties after inserting a new node.
def fix_insert(node):
    # Case 1: If the current node is the root, color it black
    if node.parent is None:
        node.color = "black"
        return node

    # Case 2: If the parent node is black, the tree is still valid
    if node.parent.color == "black":
        return node

    # Get the grandparent and uncle nodes
    grandparent = node.parent.parent
    uncle = grandparent.left if node.parent == grandparent.right else grandparent.right

    # Case 3: If the parent and uncle are red, recolor the parent, uncle, and grandparent
    if uncle and uncle.color == "red":
        node.parent.color = "black"
        uncle.color = "black"
        grandparent.color = "red"
        return fix_insert(grandparent)

    # Case 4: If the parent is red, but the uncle is black or NULL
    if node.parent == grandparent.left:
        if node == node.parent.right:
            # Left-right case, perform left rotation on parent
            node = rotate_left(node.parent)
            node = node.left
        # Left-left case, perform right rotation on grandparent
        grandparent = rotate_right(grandparent)  # Update grandparent after rotation
    else:
        if node == node.parent.left:
            # Right-left case, perform right rotation on parent
            node = rotate_right(node.parent)
            node = node.right
        # Right-right case, perform left rotation on grandparent
        grandparent = rotate_left(grandparent)  # Update grandparent after rotation

    # Recolor nodes after rotations
    node.parent.color = "black"
    node.parent.left.color = "red"
    node.parent.right.color = "red"

    return node

# Function to insert a keyword into the Red-Black Tree while maintaining its properties
def insert(root, keyword):
    def insert_helper(node, keyword, parent=None):
        if node is None:
            new_node = RBNode(keyword)
            new_node.parent = parent  # Set the parent of the new node
            return new_node

        if keyword < node.keyword:
            node.left = insert_helper(node.left, keyword, node)
        elif keyword > node.keyword:
            node.right = insert_helper(node.right, keyword, node)

        return node

    root = insert_helper(root, keyword)
    # Fix Red-Black Tree properties after insertion
    root = fix_insert(root)

    return root

# Function to search for a keyword in the Red-Black Tree
def search(root, keyword):
    if root is None or root.keyword == keyword:
        return root is not None

    if keyword < root.keyword:
        return search(root.left, keyword)
    else:
        return search(root.right, keyword)

# Function to build the Red-Black Tree from a list of keywords
def build_bst(keywords):
    root = None
    for keyword in keywords:
        root = insert(root, keyword)
    return root

# Function to count the occurrences of keywords in a list of data and measure search time
def count_hits_with_RBT(data, keywords):
    root = build_bst(keywords)
    hit_counter = 0

    start_time = time.perf_counter()
    for element in data:
        for keyword in keywords:
            if search(root, keyword) and keyword in element.lower():
                hit_counter += 1
                # print("RBT: "+keyword)
                break

    end_time = time.perf_counter()
    search_time = end_time - start_time

    return hit_counter, search_time

# Trie Node
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

# Trie insert
def trie_insert(root, keyword):
    node = root
    for char in keyword:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.is_end_of_word = True

def is_word_boundary(text, start, end):
    return (
        (start == 0 or not text[start - 1].isalnum())
        and (end == len(text) or not text[end].isalnum())
    )

def count_hits_with_trie(data, keywords):
    trie_root = TrieNode()
    start_time = time.perf_counter()

    # Insert keywords into the Trie
    for keyword in keywords:
        trie_insert(trie_root, keyword)

    hit_counter = 0
    hit_keywords = []  # List to store hit keywords

    for element in data:
        for i in range(len(element)):
            node = trie_root
            j = i
            while j < len(element) and element[j] in node.children:
                node = node.children[element[j]]
                if node.is_end_of_word and is_word_boundary(element, i, j + 1):
                    hit_counter += 1
                    hit_keywords.append(element[i : j + 1])  # Add hit keyword to the list
                j += 1

    end_time = time.perf_counter()
    search_time = end_time - start_time

    return hit_counter, search_time, hit_keywords

# KMP algorithm
def compute_prefix_table(pattern):
    prefix_table = [0] * len(pattern)
    j = 0

    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix_table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix_table[i] = j

    return prefix_table

def kmp_search(text, pattern):
    prefix_table = compute_prefix_table(pattern)
    j = 0
    hits = 0

    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = prefix_table[j - 1]
        if text[i] == pattern[j]:
            j += 1
            if j == len(pattern):
                hits += 1
                j = prefix_table[j - 1]
    return hits

def count_hits_by_kmp(data, keywords):
    hit_counter = 0
    start_time = time.perf_counter()

    for element in data:
        for keyword in keywords:
            hits = kmp_search(element.lower(), keyword)
            if hits > 0:
                hit_counter += 1
                break
    
    end_time = time.perf_counter()
    search_time = end_time - start_time

    return hit_counter, search_time

import time

def linear_search_special_character(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def count_hits_with_linear_search_special(arr1):
    start = time.perf_counter()
    special_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    special_chars_ascii_numbers = sorted([ord(char) for char in special_chars])
    hits = 0
    arr1_sorted = sorted(arr1)  # Create a sorted copy of the input array
    for num in special_chars_ascii_numbers:
        index = linear_search_special_character(arr1_sorted, num)
        while index != -1:
            hits += 1
            arr1_sorted.pop(index)  # Remove the found element to avoid counting duplicates
            index = linear_search_special_character(arr1_sorted, num)
    end = time.perf_counter()
    search = end - start
    return hits, search

def linear_search_keyword(data, keyword):
    hits = 0
    hit_keywords = []  # List to store hit keywords

    for element in data:
        for i in range(len(element)):
            j = i
            keyword_index = 0
            while j < len(element) and keyword_index < len(keyword) and element[j].lower() == keyword[keyword_index].lower():
                j += 1
                keyword_index += 1

            if keyword_index == len(keyword):
                # print(keyword)
                hits += 1
                hit_keywords.append(''.join(element[i:j]))  # Add hit keyword to the list

    return hits, hit_keywords

def arr_word_by_word(word):
    wording_array = word.split()

    output_array = []

    for word in wording_array:
        temp_word = ''
        for char in word:
            if char.isalpha() or char.isdigit():
                temp_word += char.lower()
            else:
                if temp_word:
                    output_array.append(temp_word)
                temp_word = ''
                output_array.append(char)
        if temp_word:
            output_array.append(temp_word)
    return output_array

def perform_result_with_BS(text):
    ascii_numbers = sorted([ord(char) for char in text])
    hits, timing = count_hits_with_BS(ascii_numbers)
    print("Total hits for special character(BS): "+str(hits))
    print("Total time spend for searching(BS): "+str(timing))

def perform_result_with_BST(text, keywords):
    arr_word = arr_word_by_word(text)
    hits, timing = count_hits_with_RBT(arr_word, keywords)
    print("Total hits for keywords(BST): "+str(hits))
    print("Total time spend(BST): " +str(timing))

def perform_result_with_Trie(text, keywords):
    arr_word = arr_word_by_word(text)
    hits, timing, arr_hit_keywords = count_hits_with_trie(arr_word, keywords)
    print("Total hits for keywords(Trie): "+str(hits))
    print("Total time spend(Trie): " +str(timing))

def perform_result_with_kmp(text, keywords):
    arr_word = arr_word_by_word(text)
    hits, timing = count_hits_by_kmp(arr_word, keywords)
    print("Total hits for keywords(KMP): "+str(hits))
    print("Total time spend(KMP): " +str(timing))

def perform_result_with_linear_search_special_character(text):
    ascii_numbers = sorted([ord(char) for char in text])
    hits, timing = count_hits_with_linear_search_special(ascii_numbers)
    print("Total hits for special character(Linear Search): " + str(hits))
    print("Total time spent for searching(Linear Search): " + str(timing))

def perform_result_with_linear_search_keyword(text, keywords):
    arr_word = arr_word_by_word(text)
    start_time = time.perf_counter()
    total_hits = 0
    hit_keywords = []

    for keyword in keywords:
        hits, hit_kw = linear_search_keyword(arr_word, keyword.lower())
        total_hits += hits
        hit_keywords.extend(hit_kw)

    end_time = time.perf_counter()
    search_time = end_time - start_time

    print("Total hits for keywords(Linear Search): " + str(total_hits))
    print("Total time spent(Linear Search): " + str(search_time))

    return total_hits, search_time, hit_keywords

# text =  input("Enter MEssage: ")
text = "Winnerking88sg.com Any interested Cash/Credit Acc Avail For *Soccer *Slot & Live C@sino *Horse Wlc bonus 30% High reb@te bonus 0 Deposit Wkbet.wasap.my Jeff"
text = text.lower()

data = [
    "2016", "2017", "access", "account", "admin", "administration", "airline", "alert", "and", "assistant", "authorize",
    "banking", "billing", "bills", "branch", "calculations", "card", "care", "cargo", "center", "certificate", "charged",
    "cheap", "city", "collection", "com", "commercial", "confirm", "confirmation", "contact", "copy", "credit", "customer",
    "debt", "delivery", "detail", "denied", "document", "energy", "express", "fedex", "finance", "financial", "find", "follow",
    "for", "free", "groups", "help", "http", "idnotification", "inc", "income", "info", "insurance", "intelligence", "international",
    "invoice", "label", "limitation", "limited", "load", "lock", "locked", "logging", "login", "mail", "manage", "music", "my", "news",
    "no", "notification", "notify", "online", "operation", "owner", "payment", "perfect", "policies", "post", "postal", "parcel",
    "protection", "query", "record", "redirect", "register", "replay", "required", "resolution", "resolved", "safe", "secure", "secured",
    "service", "services", "setup", "shipment", "shop", "sign", "ssl", "state", "statement", "status", "summary", "suport", "support",
    "security", "tax", "ticket", "transaction", "transportation", "travel", "unauthorized", "update", "urgency", "verificatie",
    "verification", "verified", "verify", "verifycatlons", "virtual", "webscr", "world", "activation", "configuration", "resolve",
    "decline", "declined", "review", "reactive", "activity", "setting", "archive", "recover", "manage", "managed", "unlocked",
    "suspend", "located", "insecure", "restore", "solution", "provider", "official", "protect", "direct", "home", "unlock",
    "mail", "email", "media", "store", "stores", "device", "cancel", "alert", "edit", "editted", "mobile", "modify", "remove",
    "help", "date", "signin", "unknown", "about", "notice", "limit", "asset", "server", "user", "html", "http", "identification",
    "2016", "2017", "erisim", "hesap", "sunucu", "server", "yonetim", "admin", "alarm", "banka", "fatura", "odeme", "kart", "card",
    "bakim", "kargo", "cargo", "merkez", "sertifika", "certificate", "yukle", "ucuz", "ticari", "onayla", "kopya", "kredi", "musteri",
    "borc", "sorgulama", "detay", "teslim", "belge", "detay", "maliye", "takip", "uyari", "gelir", "bilgi", "sigorta", "etiket", "kilit",
    "guvenli", "oturum", "posta", "muzik", "bildirim", "kayit", "yonlendirme", "kasa", "emniyet", "hizmet", "kurmak", "destek", "vergi",
    "islem", "yetkisiz", "guncellestirme", "dogrulama", "sanal", "engellendi", "arsiv", "medya", "magaza", "depo", "ticaret", "tarih",
    "kullanici", "kimlik", "isube", "webmail", "mail"
]


keywords = ["wlc", "bonus", "bet", "cash", "slot", "live", "high", "wasap",
            "deposit", "avail", "horse", "wkbet", "work", "easy", "money", "reliable", "licensed",
            "licenced", "repayment", "link", "free", "fill", "detail", "peronsal", "loan", "n0", "dep0sit", "$5oo",
            "cred1t", "week1y", "acct", "b0nus", "credit","urgent","failure","congratulations","giveaway","personal","information",
            "expires","security", "verification", "update", "account", "issue", "suspicious", "activity", "unauthorized", "access",
            "won","below","click","refund", "transaction", "payment", "billing", "invoice", "withdraw", "balance", "banking",
            "reset", "password", "login", "username", "hacked", "compromised", "virus", "malware", "admin", "administer", "administrator", "official", \
            "government", "irs", "hmrc", "attempt", "phishing", "scam", "fraud", "spoof", "spoofing", "phisher", "phisherman",
            "winer","pr1ze", "ver1fy", "l0gin", "passw0rd","received","need","help","pin","bank","gift","card","higher","specialize",
            "email","parcel","arriving"]

keywords.sort()
perform_result_with_BS(text)
perform_result_with_linear_search_special_character(text)

perform_result_with_BST(text, keywords)
perform_result_with_Trie(text, keywords)
perform_result_with_kmp(text, keywords)
perform_result_with_linear_search_keyword(text, keywords)
    
# trie_hit, timing, arr_hit_keywords = count_hits_with_trie(arr_word_by_word(text), keywords)
# ascii_numbers = sorted([ord(char) for char in text])
# hits, timing = count_hits_with_linear_search_special(ascii_numbers)
# # print(arr_hit_keywords)
# if(trie_hit == 0):
#     print("No suspicious keyword found")
# else:
#     print("Total Phising keyword sported: "+str(trie_hit + hits) + " / " + str(len(arr_word_by_word(text))))