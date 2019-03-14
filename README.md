# cert_bits

Python script to check nr of bits in the serial number. 

Created because of : 

- https://adamcaudill.com/2019/03/09/tls-64bit-ish-serial-numbers-mass-revocation/ 
- https://groups.google.com/d/msg/mozilla.dev.security.policy/nnLVNfqgz7g/6I1et_O9BQAJ 

**Be aware!! calling underscore prefixed functions is generally a no-no, they're intended for internal use only, and there aren't the same guarantees that the function signature will stay the same from version to same version**

# Usage 

Check a DER (crt cer der) file 

```python cert_bits.py file <certificate file>```

Check a server/url 

```python cert_bits.py url <fqdn:port>```

# Public certs 

Certificate's from public facing website can be checked at https://crt.sh 
