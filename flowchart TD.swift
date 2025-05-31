flowchart TD
    A[Start - Launch GUI Application] --> B[Display Main Window]
    
    B --> C{User Choice}
    C -->|Text Encryption| D[Enter Text in Input Field]
    C -->|Text Decryption| E[Enter Encrypted Text]
    C -->|Image Encryption| F[Enter Key 0-255]
    C -->|Image Decryption| G[Enter Key 0-255]
    
    %% Text Encryption Flow
    D --> H{Text Input Empty?}
    H -->|Yes| I[Show Warning: Enter Text First]
    H -->|No| J[Generate New Fernet Key]
    J --> K[Save Key to secret.key File]
    K --> L[Encrypt Text with Fernet]
    L --> M[Display Encrypted Text]
    M --> N[Show Success Message]
    
    %% Text Decryption Flow
    E --> O{Encrypted Text Empty?}
    O -->|Yes| P[Show Warning: Enter Encrypted Text]
    O -->|No| Q[Load Key from secret.key]
    Q --> R{Key File Exists?}
    R -->|No| S[Show Error: Key File Not Found]
    R -->|Yes| T[Decrypt Text with Fernet]
    T --> U{Decryption Successful?}
    U -->|No| V[Show Error: Decryption Failed]
    U -->|Yes| W[Display Decrypted Text]
    
    %% Image Encryption Flow
    F --> X{Key Valid? 0-255}
    X -->|No| Y[Show Warning: Key Must be 0-255]
    X -->|Yes| Z[Open File Dialog for Image]
    Z --> AA{Image Selected?}
    AA -->|No| BB[Cancel Operation]
    AA -->|Yes| CC[Read Image File as Bytes]
    CC --> DD[XOR Each Byte with Key]
    DD --> EE[Save as encrypted_filename]
    EE --> FF[Show Success Message]
    
    %% Image Decryption Flow
    G --> GG{Key Valid? 0-255}
    GG -->|No| HH[Show Warning: Key Must be 0-255]
    GG -->|Yes| II[Open File Dialog for Encrypted Image]
    II --> JJ{Image Selected?}
    JJ -->|No| KK[Cancel Operation]
    JJ -->|Yes| LL[Read Encrypted Image as Bytes]
    LL --> MM[XOR Each Byte with Key]
    MM --> NN[Save as decrypted_filename]
    NN --> OO[Show Success Message]
    
    %% Return to main menu
    I --> C
    N --> C
    P --> C
    S --> C
    V --> C
    W --> C
    BB --> C
    FF --> C
    Y --> C
    HH --> C
    KK --> C
    OO --> C
    
    %% Helper Functions
    subgraph "Helper Functions"
        PP[generate_key - Create Fernet Key]
        QQ[load_key - Read Key from File]
        RR[xor_encrypt_decrypt_image - XOR Operation]
    end
    
    %% Styling
    classDef startEnd fill:#e1f5fe
    classDef process fill:#f3e5f5
    classDef decision fill:#fff3e0
    classDef warning fill:#ffebee
    classDef success fill:#e8f5e8
    
    class A,B startEnd
    class D,E,F,G,J,K,L,Q,T,CC,DD,EE,LL,MM,NN process
    class C,H,O,R,U,X,AA,GG,JJ decision
    class I,P,S,V,Y,HH warning
    class M,N,W,FF,OO success