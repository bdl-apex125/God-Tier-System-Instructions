<Prompt>
	<Title>BDL Apex Prime 2 (CO-STAR)</Title>
	<Confidence>0.95</Confidence>
	<Tags>co-star,framework,usage</Tags>
 	<Creator>imron GTK thai</Creator>
	<ExampleInput>Summarize CO-STAR in one sentence.</ExampleInput>
	<ExampleOutput>CO-STAR is a structured framework (Context, Objective, Style, Tone, Audience, Response) that enforces clear, measurable, and reusable outputs.</ExampleOutput>
</Prompt>

📝 เอกสารชี้แจง System Instructions: BDL Apex Prime v3.0

ส่วนที่ 2: คู่มือการใช้งานและปรัชญา CO-STAR
ส่วนนี้จะกล่าวถึงวิธีการนำ System Instructions ไปใช้งานจริง และเจาะลึกปรัชญาเบื้องหลังที่ใช้ในการออกแบบ Output ทั้งหมด นั่นคือ Framework: CO-STAR
🛠 Usage: วิธีการนำไปใช้
การใช้งาน System Instructions ชุดนี้ถูกออกแบบมาให้เป็น "Zero-Setup"
 * คัดลอก (Copy): คัดลอกเนื้อหา System Instructions ทั้งหมด
 * วาง (Paste): วางเนื้อหาดังกล่าวในช่อง System Instructions (หรือ System Prompt) ของแพลตฟอร์ม LLM
 * เปิดใช้งาน (Activate): ระบบจะทำงานทันที และ LLM จะปรับโหมดการทำงานเป็น BDL Apex Prime v3.0 โดยอัตโนมัติ
ข้อแนะนำ: เนื่องจาก LLM ถูกตั้งค่าให้มี Adaptive Personas ผู้ใช้งานจึงสามารถสื่อสารด้วยภาษาปกติได้เลย ระบบจะเลือก Persona และ Tone (Hyper-intelligent) ที่เหมาะสมให้เอง
🧠 Philosophy: The CO-STAR Framework (แม่พิมพ์คุณภาพ)
CO-STAR คือมาตรฐานบังคับที่ใช้ในการสร้าง Output ทุกชิ้น เพื่อให้แน่ใจว่าคำตอบที่ส่งมอบมีโครงสร้างที่ชัดเจน สามารถวัดผลได้ และมีคุณภาพสูงที่สุด เปรียบเสมือนเป็น "พิมพ์เขียว" ของทุกการสื่อสาร
| องค์ประกอบ | คำอธิบายโดยละเอียด | การควบคุม LLM |
|---|---|---|
| C (Context) | บริบทแวดล้อม: LLM ต้องเข้าใจว่าคำถามนี้เกิดขึ้นในสภาพแวดล้อมหรือสถานการณ์ใด เช่น ถามเรื่อง "บล็อกเชน" บริบทคือ "Finance Technology" | บังคับให้ LLM ดึงความรู้เฉพาะทางของบริบทนั้นมาใช้งานเท่านั้น |
| O (Objective) | เป้าหมายที่วัดผลได้: ผลลัพธ์ที่ชัดเจนที่สุดที่ผู้ใช้ต้องการ เช่น การ "เปรียบเทียบ 3 ตัวเลือก" หรือ "สร้างสรุป 250 คำ" | คำตอบต้องโฟกัสที่การบรรลุเป้าหมายนี้ และตัดข้อมูลที่ไม่เกี่ยวข้องออกไป |
| S (Style) | สไตล์การเขียน: กำหนดรูปแบบภาษา เช่น Academic Style (วิชาการ), Technical Report (รายงานเทคนิค), หรือ Conversational Blog (บทความสบาย ๆ) | ควบคุมการใช้คำศัพท์และโครงสร้างประโยคให้เหมาะสมกับงาน |
| T (Tone) | น้ำเสียง: กำหนดอารมณ์ของการสื่อสาร เช่น Hyper-intelligent (ฉลาด, มั่นใจ), Empathetic (เห็นอกเห็นใจ), หรือ Formal (เป็นทางการ) | ควบคุมอารมณ์และระดับความมั่นใจที่แสดงออกในคำตอบ |
| A (Audience) | กลุ่มเป้าหมาย: LLM ต้องปรับระดับความซับซ้อนตามความรู้พื้นฐานของผู้รับสาร เช่น Audience คือ "ผู้บริหารที่ไม่ใช่สายเทคนิค" การอธิบายต้องง่ายและเน้น Business Impact | ปรับระดับภาษาและศัพท์เฉพาะทาง (Jargon) ให้เหมาะสม |
| R (Response) | รูปแบบผลลัพธ์ที่กำหนดโครงสร้าง: เป็นการกำหนด Output Format ที่แน่นอน เช่น Markdown Table, JSON Array, Single HTML File หรือ Code Block | บังคับให้ Output มีโครงสร้างที่แน่นอนและสามารถนำไปใช้งานต่อได้ทันที (Zero-Latency for next step) |
