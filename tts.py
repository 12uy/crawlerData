import json

import requests


def textToSpeech(payload):
    url = 'https://api.fpt.ai/hmi/tts/v5'

    payload = payload.replace("\n", " ")

    api_key = 'L0L9gx92DEnoQZa7Bp0MrPYLpJ6ouxFy' # api key lấy từ fpt.ai

    headers = {
        'api-key': api_key,
        'speed': '',
        'voice': 'banmai'
    }

    response = requests.request('POST', url, data=payload.encode('utf-8'), headers=headers).json()
    linkTTS = response['async']  # lấy ra link mp3 từ json trả về
    return linkTTS

# payload = '''Theo đại diện Phòng Cảnh sát giao thông - Công an TP Hà Nội, lực lượng CSGT sẽ huy động 100% quân số làm nhiệm vụ, đảm bảo giao thông thông suốt, đặc biệt tại các tuyến đường quanh sân vận động Mỹ Đình.Sau trận đấu, lực lượng CSGT sẽ phối hợp với các đơn vị chức năng Công an Hà Nội đảm bảo trật tự an toàn giao thông, phòng, chống đua xe trái phép. Các tổ công tác 141 sẽ cắm chốt công khai trên địa bàn các quận nội thành và tuần tra hóa trang trên địa bàn quận Hoàn Kiếm, Đống Đa, Hai Bà Trưng để kiểm tra, kiểm soát, phòng, chống đua xe trái phép, đảm bảo an ninh trật tự.Bên cạnh đó, lực lượng CSGT sẽ phối hợp với Trung đoàn Cảnh sát cơ động, Cảnh sát 113 (Công an TP Hà Nội), công an các địa bàn chủ động tuần tra trên các tuyến đường.Theo phương án phân luồng của Công an Hà Nội, ngày 22/5, Công an Hà Nội hạn chế đối với các xe ô tô chở hàng có khối lượng hàng hóa chuyên chở từ 500 kg, xe ô tô chở khách từ 16 chỗ trở lên (trừ phương tiện của các lực lượng tham gia, xe có phù hiệu bảo vệ và xe giải quyết, khắc phục sự cố) lưu thông trên các tuyến đường: Lê Đức Thọ, Lê Quang Đạo, Mễ Trì, Châu Văn Liêm, Nguyễn Cơ Thạch, Đỗ Xuân Hợp, Trần Hữu Dực, Nguyễn Hoàng, Hàm Nghi, Tân Mỹ, Hồ Tùng Mậu, đường gom phải Đại lộ Thăng Long đoạn từ Trung tâm Hội nghị Quốc gia đến nút giao Lê Quang Đạo.Công an Hà Nội hướng dẫn, tổ chức phân luồng các phương tiện trong ngày diễn ra trận tranh giải Ba và trận Chung kết giữa U23 Việt Nam - U23 Thái Lan như sau:- Các phương tiện từ phía Tây sang phía Đông đến QL32 đi về trung tâm thành phố và ngược lại theo tuyến: Quốc lộ 32 - Đường 70 - Đại lộ Thăng Long (đường cao tốc hoặc đường gom trái) - Phạm Hùng - đi trung tâm thành phố.- Các phương tiện từ tỉnh Phú Thọ, Vĩnh Phúc và Hòa Bình đi trung tâm thành phố và ngược lại theo tuyến: Quốc lộ 32 - Quốc lộ 21 - Đại lộ Thăng Long - vào trung tâm thành phố.- Các phương tiện từ các tỉnh phía Nam, Đông Nam lưu thông trên tuyến Vành đai III trên cao - cầu Thăng Long - Võ Văn Kiệt - Quốc lộ 2 đi các tỉnh phía Bắc và Tây Bắc hạn chế xuống đường Hồ Tùng Mậu và đường gom phải Đại lộ Thăng Long.'''
#
# print(textToSpeech(payload))

