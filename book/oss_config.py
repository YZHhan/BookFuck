# coding = utf-8
import oss2
import os

'''
OSS:
    Python 接入OSS Version:2.6、2.7、3.3、3.4、3.5
    OSS__version__ 2.5.0
    crcmod的C的扩展模式没有安装成功，建议关闭CRC数据校验
    ————————————————————————————————————————————
基本概念介绍：
    Bucket：存储空间是您用于存储对象（Object）的容器，所有的对象都必须隶属于某个存储空间。
    Object:对象是 OSS 存储数据的基本单元，也被称为 OSS 的文件。
    Region:Region 表示 OSS 的数据中心所在的地域，物理位置。
    Endpoint:Endpoint 表示 OSS 对外服务的访问域名。
    AccessKey(访问秘钥):简称 AK，指的是访问身份验证中用到的 AccessKeyId 和AccessKeySecret。AccessKeyId 用于标识用户，AccessKeySecret 是用户用于加密签名字符串和 OSS 用来验证签名字符串的密钥，



oss2.Auth对象承载了用户的认证信息，即AccessKeyId和AccessKeySecret等；
oss2.Service对象用于服务相关的操作，目前就是用来列举Bucket；
oss2.BucketIterator对象是一个可以遍历用户Bucket信息的迭代器

'''

end_point = "http://oss-cn-beijing.aliyuncs.com"
bucket_name = "caoxiaohui"


class OSS_Config(object):

    def __init__(self):
        self.auth = oss2.Auth('LTAIjF14rh5Xlem8', 'yAJPbHSSJ6LE3IwT4BZ4eoanbiAo1S')
        self.service = oss2.Service(self.auth, 'oss-cn-beijing.aliyuncs.com')
        self.bucket = oss2.Bucket(self.auth, end_point, bucket_name, connect_timeout=300)

    def print(self):
        print(oss2.__version__)
        print([b.name for b in oss2.BucketIterator(self.service)])  # 打印  Bucket信息的迭代器

    def upload_file(self):
        print("我是文件上傳")
        result = self.bucket.put_object("001.txt", "This is my 001 file")

        # 必须以二进制的方式打开文件，因为需要知道文件包含的字节数。
        # with open('/Users/yinzh/PycharmProjects/book_fuck/book/001.txt', 'rb') as fileobj:
            # Seek方法用于指定从第1000个字节位置开始读写。上传时会从您指定的第1000个字节位置开始上传，直到文件结束。
            # fileobj.seek(1000, os.SEEK_SET)
            # Tell方法用于返回当前位置。
            # current = fileobj.tell()
            # result = self.bucket.put_object('001.txt', fileobj)


        # HTTP返回码.
        print('http status: {0}'.format(result.status))
        # 请求ID。请求ID是请求的唯一标识，强烈建议在程序日志中添加此参数。
        print('request_id: {0}'.format(result.request_id))
        # ETag是put_object方法返回值特有的属性。
        print('ETag: {0}'.format(result.etag))
        # HTTP响应头部。
        print('date: {0}'.format(result.headers['date']))


if __name__ == '__main__':
    oss2_config = OSS_Config()
    oss2_config.print()
    oss2_config.upload_file()
