import sys

def convert_file(file_path):
    try:
        with open(file_path, 'rb') as f:
            hex_content = f.read()
        
        # Read the entire file into memory and concatenate all lines into one continuous hex string
        hex_string = ''.join(line.strip() for line in hex_content)

        # Splitting the hex string into pairs of bytes
        byte_pairs = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]
        
        total_pairs = len(byte_pairs)
        print("Total number of pairs:", total_pairs)
        
        pairCounter = 3072
        chCnt = 0
        # Extracting the fields from the byte pairs
        VFile = ''.join(byte_pairs[2:6])
        NDSC = ''.join(byte_pairs[16:20])
        SInt = ''.join(byte_pairs[66:70])
        PreT = ''.join(byte_pairs[84:88])
        AfterT = ''.join(byte_pairs[88:92])
        Ecu_Id = ''.join(byte_pairs[203:204])
        NDC = ''.join(byte_pairs[220:221])
        NMD = ''.join(byte_pairs[221:222])
        TSR = ''.join(byte_pairs[1815:1819])
        
        #<-- Start Conversion Section -->
                    
        VFile_InAscii= ""
        for i in range(0, len(VFile), 2):
            VFile_InAscii += chr(int(VFile[i:i+2], 16))
        
        NDSC_InDecimal = int(NDSC,16)
        SInt_InDecimal = int(SInt,16)
        PreT_InDecimal = int(PreT,16)
        AfterT_InDecimal = int(AfterT,16)
        Ecu_Id_InDecimal = int(Ecu_Id,16)
        NDC_InDecimal = int(NDC,16)
        NMD_InDecimal = int(NMD,16)
        TSR_InDecimal = int(TSR,16)
        
        print("VFile: ", VFile_InAscii)
        print("NDSC: ", NDSC_InDecimal)
        print("SInt: ", SInt_InDecimal)
        print("PreT: ", PreT_InDecimal)
        print("AfterT: ", AfterT_InDecimal)
        print("Ecu_Id: ", Ecu_Id_InDecimal)
        print("NDC: ", NDC_InDecimal)
        print("NMD: ", NMD_InDecimal)
        print("TSR: ", TSR_InDecimal)
        
        
        
        output_path = "Mode File Parsing Result.txt"
        # Open file in "w" mode to clear its contents
        with open(output_path, "w") as f:
            pass
        with open(output_path, 'a') as file2:
                file2.write("......................................................................................................................................................... " + "\n")
                file2.write("                                                         Mode File Parser Tool                                          " + "\n")       
                file2.write("Revision History:" + "\n")     
                file2.write("Date             Author                 Description" + "\n")
                file2.write("28-07-2023       mduong                 This ModeFile content parser that decodes what ModeFile contents have been encoded and sends to SW Module " + "\n\n")

                file2.write("......................................................................................................................................................... " + "\n")
                file2.write("                                                            Header Information                                                 " + "\n")       
                file2.write("......................................................................................................................................................... " + "\n\n")        
                file2.write("VFile: " + VFile_InAscii + "\n" + "NDSC: " + str(NDSC_InDecimal) + "\n" + "SInt: " + str(SInt_InDecimal) + "\n" + "PreT: " + str(PreT_InDecimal) + "\n" + "AfterT: " + str(AfterT_InDecimal) + "\n" + "Ecu_Id: " + str(Ecu_Id_InDecimal) + "\n" + "NDC: " + str(NDC_InDecimal) + "\n" + "NMD: " + str(NMD_InDecimal) + "\n" + "TSR: " + str(TSR_InDecimal) + "\n" +"\n\n")
                
                file2.write("......................................................................................................................................................... " + "\n")
                file2.write("                                                            Channel Information                                                 " + "\n")       
                file2.write("......................................................................................................................................................... ")
        while pairCounter <= total_pairs:

            ChI = ''.join(byte_pairs[2048+chCnt:2052+chCnt])
            Addr = ''.join(byte_pairs[2752+chCnt:2764+chCnt])
            Bcnt = ''.join(byte_pairs[2814+chCnt:2815+chCnt])
            SFlag = ''.join(byte_pairs[2817+chCnt:2818+chCnt])
            RfChI = ''.join(byte_pairs[2856+chCnt:2860+chCnt])
            TgrFlag = ''.join(byte_pairs[2890+chCnt:2891+chCnt])
            TgrMode = ''.join(byte_pairs[2891+chCnt:2892+chCnt])
            TgrSlope = ''.join(byte_pairs[2892+chCnt:2893+chCnt])
            TgrType = ''.join(byte_pairs[2905+chCnt:2906+chCnt])
            TgrLevel = ''.join(byte_pairs[2906+chCnt:2914+chCnt])
            print("\n------------------------------------------\n")
            #<-- Start Conversion Section -->
            
            ChI_InDecimal = int(ChI, 16)
            Addr_InAscii= ""
            for i in range(0, len(Addr), 2):
                Addr_InAscii += chr(int(Addr[i:i+2], 16))
            Bcnt_InDecimal = int(Bcnt, 16)
            SFlag_InDecimal = int(SFlag, 16)
            
            if RfChI == 'FFFFFFFF' or RfChI == 'ffffffff':
                RfChI_InDecimal = -1
            else:
                RfChI_InDecimal = int(RfChI, 16)
                
            TgrFlag_InDecimal = int(TgrFlag, 16)
            TgrMode_InDecimal = int(TgrMode, 16)
            TgrSlope_InDecimal = int(TgrSlope, 16)
            TgrType_InDecimal = int(TgrType, 16)
            TgrLevel_InDecimal = int(TgrLevel, 16)
            
            print("ChI: ", ChI_InDecimal)
            print("Addr: ", Addr_InAscii)
            print("Bcnt: ", Bcnt_InDecimal)
            print("SFlag: ", SFlag_InDecimal)
            print("RfChI: ", RfChI_InDecimal)
            print("TgrFlag: ", TgrFlag_InDecimal)
            print("TgrMode: ", TgrMode_InDecimal)
            print("TgrSlope: ", TgrSlope_InDecimal)
            print("TgrType: ", TgrType_InDecimal)
            print("TgrLevel: ", TgrLevel_InDecimal)
            # Writing the formatted fields to file
            with open(output_path, 'a') as file2:
                file2.write("\n\n")
                
                file2.write("ChI: " + str(ChI_InDecimal) + "\n" + "Addr: " + Addr_InAscii + "\n" + "Bcnt: " + str(Bcnt_InDecimal) + "\n" + "SFlag: " + str(SFlag_InDecimal) + "\n" + "RfChI: " + str(RfChI_InDecimal) + "\n" + "TgrFlag: " + str(TgrFlag_InDecimal) + "\n" + "TgrMode: " + str(TgrMode_InDecimal) + "\n" + "TgrSlope: " + str(TgrSlope_InDecimal) + "\n" + "TgrType: " + str(TgrType_InDecimal) + "\n" + "TgrLevel: " + str(TgrLevel_InDecimal) + "\n")
            
            pairCounter += 1024
            chCnt +=1024
            

                
    except Exception:
        print("Error:")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ModeFileParser.py <file_path>")
    else:
        file_path = sys.argv[1]
        convert_file(file_path)
