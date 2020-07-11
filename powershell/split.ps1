<#
powershell split code v.1 
.Synopsis
    Split text file(s) by lines, put into each output file as many complete lines of input as possible without exceeding size bytes.
#>
function Split-FileByLine
{
    [CmdletBinding()]
    Param
    (
        [Parameter(Mandatory = $true, ValueFromPipeline = $true, ValueFromPipelineByPropertyName = $true)]
        [string[]]$FileName,

        [Parameter(ValueFromPipelineByPropertyName = $true)]
        [string]$OutPath = (Get-Location -PSProvider FileSystem).Path,

        [Parameter(Mandatory = $true, ValueFromPipelineByPropertyName = $true)]
        [long]$MaxFileSize,

        [Parameter(ValueFromPipelineByPropertyName = $true)]
        [string]$Encoding = 'Default'
    )

    Begin
    {
        # Scriptblocks for common tasks
        $DisposeInFile = {
            Write-Verbose 'Disposing StreamReader'
            $InFile.Close()
            $InFile.Dispose()
        }

        $DisposeOutFile = {
            Write-Verbose 'Disposing StreamWriter'
            $OutFile.Flush()
            $OutFile.Close()
            $OutFile.Dispose()
        }

        $NewStreamWriter = {
            Write-Verbose 'Creating StreamWriter'
            $OutFileName = Join-Path -Path $OutPath -ChildPath (
                '{0}_part_{1}{2}' -f [System.IO.Path]::GetFileNameWithoutExtension($_), $Counter, [System.IO.Path]::GetExtension($_)
            )

            $OutFile = New-Object -TypeName System.IO.StreamWriter -ArgumentList (
                $OutFileName,
                $false,
                $FileEncoding
            ) -ErrorAction Stop
            $OutFile.AutoFlush = $true
            Write-Verbose "Writing new file: $OutFileName"
        }
    }

    Process
    {
        if($Encoding -eq 'Default')
        {
            # Set default encoding
            $FileEncoding = [System.Text.Encoding]::Default
        }
        else
        {
            # Try to set user-specified encoding
            try
            {
                $FileEncoding = [System.Text.Encoding]::GetEncoding($Encoding)
            }
            catch
            {
                throw "Not valid encoding: $Encoding"
            }
        }

        Write-Verbose "Input file: $FileName"
        Write-Verbose "Output folder: $OutPath"

        if(!(Test-Path -Path $OutPath -PathType Container)){
            Write-Verbose "Folder doesn't exist, creating: $OutPath"
            $null = New-Item -Path $OutPath -ItemType Directory -ErrorAction Stop
        }

        $FileName | ForEach-Object {
            # Open input file
            $InFile = New-Object -TypeName System.IO.StreamReader -ArgumentList (
                $_,
                $FileEncoding
            ) -ErrorAction Stop
            Write-Verbose "Current file: $_"

            $Counter = 0
            $OutFile = $null

            # Read lines from input file
            while(($line = $InFile.ReadLine()) -ne $null)
            {
                if($OutFile -eq $null)
                {
                    # No output file, create StreamWriter
                    . $NewStreamWriter
                }
                else
                {
                    if($OutFile.BaseStream.Length -ge $MaxFileSize)
                    {
                        # Output file reached size limit, closing
                        Write-Verbose "OutFile lenght: $($InFile.BaseStream.Length)"
                        . $DisposeOutFile
                        $Counter++
                        . $NewStreamWriter
                    }
                }

                # Write line to the output file
                $OutFile.WriteLine($line)
            }

            Write-Verbose "Finished processing file: $_"
            # Close open files and cleanup objects
            . $DisposeOutFile
            . $DisposeInFile
        }
    }
}
$InputFile = 'C:\Users\calvin\Desktop\OCF.xml'
$OutputDir = 'C:\Users\calvin\Desktop\OCF170316split.xml'
Split-FileByLine -FileName $InputFile -OutPath $OutputDir -MaxFileSize 500.99MB
OCFsplit
.ps1
