# 🧩 Problem Set 4

## Introduction

This problem set is designed to introduce you to encryption and decryption algorithms using the Caesar cipher. Encryption is the process of making information unreadable without specific knowledge, and a cipher is an algorithm used for encryption and decryption. The Caesar cipher shifts each letter in the message by a fixed amount to generate a secret code. In this problem set, you will implement functions to encrypt and decrypt text using Caesar cipher with single-level and multi-level shifts.

## Problem 1: Encryption and Decryption

In this problem, you will implement functions to encrypt plaintext into ciphertext using the Caesar cipher. The `build_coder` function creates a dictionary that maps each letter to its shifted counterpart, while the `apply_coder` function applies the cipher to the given text. Additionally, you will implement the `apply_shift` function to apply a single-level Caesar shift to the entire text.

## Problem 2: Code-breaking

Your friend has been sending encrypted messages using the Caesar cipher, but you don't know the shift key. In this problem, you will write a function called `find_best_shift` that attempts to find the correct shift key by testing different possibilities. The function will decode the text into words from a given wordlist, and if all the words obtained are valid, the correct shift key is found.

## Problem 3: Multi-level Encryption & Decryption

To enhance security, you will implement a multi-level Caesar cipher in this problem. The function `apply_shifts` takes a text and a list of shift tuples. Each tuple represents the location to start the shift and the shift offset. The shifts are layered, meaning each one is applied from its starting position until the end of the text.
## Problem 4: Multi-level Code-breaking

Your friend has sent you another message encrypted with a multi-level Caesar cipher. In this part, you will implement the function `find_best_shifts_rec`, which uses recursion to find the shift key that will correctly decode the text to valid words from the wordlist. The shift can only begin at the start of a word.

## Problem 5: The Moral of the Story

Finally, you will use all the implemented methods to decrypt the fable given in the file `fable.txt`. After successfully decrypting the message, you will reflect on how the fable relates to your education at MIT.

---
For more information about the MIT course and licensing terms, visit the [MIT OpenCourseWare](http://ocw.mit.edu/terms).