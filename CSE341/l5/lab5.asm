
.MODEL SMALL 

.STACK 300H ; SIZE OF STACK SIZE .. H =HEX

.DATA

;a db 10     
;var db ?     

a db 1,2,3,4,5
myarr1 dw "hi this is me" 
myarr2 db 7 dup(1)    
; myarr2 db ?,?,?,?,?,?,? also valid 
msg db "Hello world!$"  

.CODE            



 
MAIN PROC     
    
MOV AX,@DATA    
MOV DS,AX  
    ; hello word cx times! ; hudai
    ;mov cx,15 
;    start: 
;    lea dx,msg
;    mov ah,9
;    int 21h
;    mov ah,2
;    mov dl,0Ah
;    int 21h
;    mov dl,0Dh
;    int 21h
;    loop start       
;     
     
     
     ;array usign index 1   
     
     mov ah,2 
     ; array index in si
     mov si,4  
     mov cx,5
     start: 
     ; access value in array
     mov dl,a[si]
     ; print it 
     add dl,30h 
     int 21h
     ; update si
     dec si     
     loop start
     
     
     ;array using pointers 2
     
     ;mov ah,2 
;     lea si,a
;     
;     mov dl,[si]     
;     add dl,30h
;     int 21h   
;     add si,1 ; add si,2 for dw (word)
     
     
     
     ; stack  
     ;push source ; source as ax,bx,cx,dx
     ;pop destination  
     
     
     
     
     
     
     
     
     
     
     

    
     exit:    ; etaw hudai
    
MOV AX,4C00H
INT 21H
MAIN ENDP
    END MAIN  
    

    