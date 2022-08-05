
.MODEL SMALL 

.STACK 100H 

.DATA

arr2 db 5 dub(?)


.CODE            
 
MAIN PROC     
MOV AX,@DATA    
MOV DS,AX  
; take 5 inputs
   mov ah,1 
   mov si,0 
   mov cx,5
   start:
   int 21h
   mov arr2[si],al
   inc si   
   loop start:
   
   mov si,4
   mov ah,2
   mov cx,5
   start2:
   mov dl,arr2[si]
   dec si
   int 21h  
   loop start2
   
   
   ;mov cx,4 
   
   ;start:
   ;mov dl,arr1[si] 
  ; add dl,30h 
;   int 21h
;   add si,2
;   loop start




    
    
MOV AX,4C00H
INT 21H
MAIN ENDP
    END MAIN  
    

    