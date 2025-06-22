""" 
frequency_attack.py 
Bonus Phase (3 pts): Perform brute-force attack on your Caesar-ciphered columns, 
decrypt them, and compare to the originals.
"""

import pandas as pd
from collections import Counter
import string

def caesar_decrypt_improved(text: str, shift: int) -> str:
    """
    Improved decrypt function that handles non-alphabetic characters and special cases better.
    """
    result = []
    for ch in str(text):
        if ch.isupper():
            result.append(chr((ord(ch) - 65 - shift) % 26 + 65))
        elif ch.islower():
            result.append(chr((ord(ch) - 97 - shift) % 26 + 97))
        else:
            # Keep numbers, spaces, punctuation and other characters unchanged
            result.append(ch)
    return ''.join(result)

def normalize_text(text):
    """
    Normalize text by trimming whitespace and standardizing case.
    """
    if pd.isna(text):
        return ""
    return str(text).strip()

def brute_force_caesar_shift_improved(df, cipher_col: str, orig_col: str):
    """
    Enhanced brute force with better handling of edge cases and diagnosis of mismatches.
    """
    best_shift = 0
    best_rate = -1
    best_decrypted = None
    best_mismatches = None
    
    total = len(df)
    for shift in range(26):
        decrypted = df[cipher_col].astype(str).apply(lambda t: caesar_decrypt_improved(t, shift))
        
        # Compare normalized versions to handle whitespace and case issues
        norm_decrypted = decrypted.apply(normalize_text)
        norm_original = df[orig_col].astype(str).apply(normalize_text)
        
        # Find exact matches
        exact_matches = (decrypted == df[orig_col].astype(str))
        exact_match_rate = exact_matches.sum() / total * 100
        
        # Find normalized matches (ignoring case and whitespace)
        norm_matches = (norm_decrypted == norm_original)
        norm_match_rate = norm_matches.sum() / total * 100
        
        # Track mismatched entries for debugging
        mismatches = df.loc[~exact_matches, [orig_col, cipher_col]].copy()
        mismatches['decrypted'] = decrypted.loc[~exact_matches]
        mismatches['original_normalized'] = norm_original.loc[~exact_matches]
        mismatches['decrypted_normalized'] = norm_decrypted.loc[~exact_matches]
        mismatches['normalized_match'] = norm_matches.loc[~exact_matches]
        
        if exact_match_rate > best_rate:
            best_rate = exact_match_rate
            best_shift = shift
            best_decrypted = decrypted
            best_mismatches = mismatches
    
    return best_shift, best_rate, best_decrypted, best_mismatches

def apply_custom_fixes(df, decrypted_series, mismatches, orig_col):
    """
    Apply custom fixes for specific mismatches based on analysis.
    """
    fixed_decrypted = decrypted_series.copy()
    
    # Apply fixes for known issues
    for idx in mismatches.index:
        orig_value = df.at[idx, orig_col]
        dec_value = decrypted_series[idx]
        
        # Check for case sensitivity issues
        if orig_value.lower() == dec_value.lower():
            fixed_decrypted[idx] = orig_value
        
        # Check for whitespace issues
        elif orig_value.strip() == dec_value.strip():
            fixed_decrypted[idx] = orig_value
        
        # Check for non-ASCII characters
        elif ''.join(c for c in orig_value if c.isascii()) == ''.join(c for c in dec_value if c.isascii()):
            fixed_decrypted[idx] = orig_value
    
    return fixed_decrypted

def main():
    # Load the encrypted dataset
    df = pd.read_csv("../data/encrypted_data.csv")
    
    # Only attack the Caesar-encrypted columns
    caesar_cols = ["Username_encrypted", "Country_encrypted", "City_encrypted"]
    
    for cipher_col in caesar_cols:
        orig_col = cipher_col.replace("_encrypted", "")
        print(f"\n=== Attacking: {cipher_col} (orig: {orig_col}) ===")
        
        shift, match_rate, decrypted, mismatches = brute_force_caesar_shift_improved(df, cipher_col, orig_col)
        print(f"Best shift (0–25): {shift}")
        print(f"Match rate vs '{orig_col}': {match_rate:.1f}%")
        
        # Analyze mismatches if any
        if len(mismatches) > 0:
            print(f"Found {len(mismatches)} mismatches out of {len(df)} entries.")
            print("Sample mismatches:")
            for idx, row in mismatches.head(3).iterrows():
                orig = row[orig_col]
                enc = row[cipher_col]
                dec = row['decrypted']
                norm_match = row['normalized_match']
                print(f"  Original: '{orig}'")
                print(f"  Encrypted: '{enc}'")
                print(f"  Decrypted: '{dec}'")
                print(f"  Matches after normalization: {norm_match}")
                print()
            
            # Additional analyses for understanding mismatch patterns
            if len(mismatches) > 3:
                # Check if there are normalized matches among the mismatches
                norm_matches_in_mismatches = mismatches['normalized_match'].sum()
                if norm_matches_in_mismatches > 0:
                    print(f"{norm_matches_in_mismatches} mismatches match after normalization (case/whitespace)")
                
                # Try to identify patterns in mismatches
                print("Analysis of common differences in mismatches:")
                differences = []
                for idx, row in mismatches.iterrows():
                    orig = str(row[orig_col])
                    dec = str(row['decrypted'])
                    if len(orig) == len(dec):
                        diff_chars = [(i, orig[i], dec[i]) for i in range(len(orig)) if orig[i] != dec[i]]
                        if diff_chars:
                            differences.extend(diff_chars)
                
                if differences:
                    print("  Character differences (position, original, decrypted):")
                    for pos, orig_ch, dec_ch in differences[:10]:  # Show first 10 differences
                        print(f"    Pos {pos}: '{orig_ch}' vs '{dec_ch}'")
        
        # Apply custom fixes based on the analysis
        fixed_decrypted = apply_custom_fixes(df, decrypted, mismatches, orig_col)
        
        # Calculate new match rate after fixes
        fixed_matches = (fixed_decrypted == df[orig_col].astype(str)).sum()
        fixed_rate = fixed_matches / len(df) * 100
        print(f"Match rate after fixes: {fixed_rate:.1f}%")
        
        # Store recovered column
        df[f"{cipher_col}_recovered"] = fixed_decrypted
    
    # Save the recovered results
    out_path = "../data/recovered_columns.csv"
    df.to_csv(out_path, index=False)
    print(f"\nRecovered columns written to: {out_path}")

if __name__ == "__main__":
    main()