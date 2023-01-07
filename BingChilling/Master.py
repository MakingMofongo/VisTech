import theChilling
import concurrent.futures

Processor = concurrent.futures.ProcessPoolExecutor()
Future_Chilling = Processor.submit(theChilling.main())