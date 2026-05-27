
# Ý tưởng xử lý:
# - Dùng List để lưu danh sách bài hát
# - append() để thêm cuối danh sách
# - insert() để chèn vào vị trí cụ thể
# - remove() / pop() để xóa bài hát
# - sort() để sắp xếp A-Z
# - slicing [:3] để lấy 3 bài đầu tiên
# - enumerate() để hiển thị STT đẹp hơn

playlist = []

while True:
    print('========= MENU QUẢN LÝ DANH SÁCH PHÁT =========')
    print('1. Thêm bài hát vào danh sách phát               ')
    print('2. Xem danh sách phát                            ')
    print('3. Xóa bài hát khỏi danh sách                    ')
    print('4. Sắp xếp và trích xuất danh sách               ')
    print('5. Thoát chương trình                            ')
    print('=================================================')

    choose = input('Nhập lựa chọn của bạn: ')

    if choose == '1':
        print('--- THÊM BÀI HÁT ---')
        print('1. Thêm vào cuối danh sách')
        print('2. Chèn vào vị trí cụ thể')

        sub_insert_choose = input('Nhập lựa chọn: ')

        if sub_insert_choose == '1':
            song = input('Nhập tên bài hát: ')
            playlist.append(song)

            print('Bài hát đã được thêm vào cuối danh sách phát')
            print(f'Số lượng bài hát: {len(playlist)}')

        elif sub_insert_choose == '2':
            song = input('Nhập tên bài hát: ')
            pos = int(input('Nhập vị trí cần chèn: '))

            if 0 <= pos <= len(playlist):
                playlist.insert(pos, song)

                print('Bài hát đã được chèn vào danh sách phát')
                print(f'Số lượng bài hát: {len(playlist)}')
            else:
                print('Vị trí không hợp lệ.')

        else:
            print('Lựa chọn không hợp lệ.')

    elif choose == '2':
        print('--- DANH SÁCH PHÁT ---')

        for i, song in enumerate(playlist, start=1):
            print(f"{i}. {song}")

        print(f'\nSố lượng bài hát: {len(playlist)}')

    elif choose == '3':
        print('--- XÓA BÀI HÁT ---')
        print('1. Xóa theo tên bài hát')
        print('2. Xóa theo số thứ tự')

        sub_delete_choose = input('Nhập lựa chọn: ')

        if sub_delete_choose == '1':
            song = input('Nhập tên bài hát cần xóa: ')

            if song in playlist:
                playlist.remove(song)
                print(f'Đã xóa bài hát {song} khỏi danh sách')
            else:
                print('Bài hát không tồn tại trong danh sách phát')

        elif sub_delete_choose == '2':
            pos = int(input('Nhập số thứ tự của bài hát cần xóa: '))

            if 1 <= pos <= len(playlist):
                deleted_song = playlist.pop(pos - 1)
                print(f'Đã xóa bài hát {deleted_song} khỏi danh sách')
            else:
                print('Số thứ tự không hợp lệ')

        else:
            print('Lựa chọn không hợp lệ.')

    elif choose == '4':
        print('--- SẮP XẾP VÀ TRÍCH XUẤT DANH SÁCH ---')
        print('1. Sắp xếp danh sách phát theo bảng chữ cái A-Z')
        print('2. Hiển thị 3 bài hát đầu tiên')

        sub_sort_choose = input('Nhập lựa chọn: ')

        if sub_sort_choose == '1':
            playlist.sort()

            print('--- DANH SÁCH PHÁT SAU KHI SẮP XẾP ---')

            for i, song in enumerate(playlist, start=1):
                print(f"{i}. {song}")

        elif sub_sort_choose == '2':
            print('--- 3 BÀI HÁT ĐẦU TIÊN ---')

            for i, song in enumerate(playlist[:3], start=1):
                print(f"{i}. {song}")

        else:
            print('Lựa chọn không hợp lệ.')

    elif choose == '5':
        print('Cảm ơn bạn đã sử dụng dịch vụ. Tạm biệt!')
        break

    else:
        print('Lựa chọn không hợp lệ. Vui lòng chọn lại.')